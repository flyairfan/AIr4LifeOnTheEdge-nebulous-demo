# server/edge_command_server.py
from flask import Flask, jsonify, request
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from drone_control.drone_control import start_mission
import os
import logging
from logging.handlers import RotatingFileHandler

# Initialize Flask application
app = Flask(__name__)

# ========== SECURITY CONFIGURATION ==========
csp = {
    'default-src': "'self'",
    'script-src': "'self'",
    'style-src': "'self' 'unsafe-inline'"
}
Talisman(app, 
         content_security_policy=csp,
         force_https=os.getenv('FLASK_ENV') == 'production')

# ========== RATE LIMITING ==========
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["120 per minute", "2 per second"],
    storage_uri="memory://"
)

# ========== PRODUCTION LOGGING ==========
logger = logging.getLogger("edge_command_server")
logger.setLevel(logging.INFO)

# Console handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
))

# Rotating file handler (5MB files, keep 3 backups)
file_handler = RotatingFileHandler(
    'edge_command.log',
    maxBytes=5*1024*1024,
    backupCount=3,
    encoding='utf-8'
)
file_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
))

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# ========== HEALTH ENDPOINT ==========
@app.route('/health')
@limiter.exempt
def health_check():
    """Kubernetes-compatible health check endpoint"""
    return jsonify({
        "status": "healthy",
        "version": "1.3.0",
        "components": {
            "drone_control": True,
            "sensor_interface": True
        }
    }), 200

# ========== MISSION CONTROL ENDPOINT ==========
@app.route("/start_mission", methods=["POST"])
@limiter.limit("5/minute")  # Stricter limit for critical operations
def trigger_mission():
    """
    Secured endpoint to initiate drone cleaning missions
    Requires JSON payload with authorization token
    """
    try:
        # ===== REQUEST VALIDATION =====
        if not request.is_json:
            logger.warning("Invalid content type from %s", request.remote_addr)
            return jsonify({
                "status": "error",
                "code": "INVALID_CONTENT_TYPE",
                "message": "Content-Type must be application/json"
            }), 415

        payload = request.get_json()
        
        # ===== AUTHORIZATION CHECK =====
        if not validate_authorization(payload.get('token')):
            logger.warning("Unauthorized request from %s", request.remote_addr)
            return jsonify({
                "status": "error",
                "code": "UNAUTHORIZED",
                "message": "Valid authorization token required"
            }), 401

        # ===== MISSION EXECUTION =====
        logger.info("Initiating mission from %s", request.remote_addr)
        mission_result = start_mission()
        
        if "failed" in mission_result.lower():
            logger.error("Mission failure: %s", mission_result)
            return jsonify({
                "status": "error",
                "code": "MISSION_FAILURE",
                "message": mission_result
            }), 500

        logger.info("Mission success: %s", mission_result)
        return jsonify({
            "status": "success",
            "code": "MISSION_COMPLETE",
            "message": mission_result
        }), 200

    except Exception as e:
        logger.critical("System failure: %s", str(e), exc_info=True)
        return jsonify({
            "status": "error",
            "code": "INTERNAL_ERROR",
            "message": "System malfunction - contact support"
        }), 500

def validate_authorization(token: str) -> bool:
    """Validate authorization token (stub for production implementation)"""
    # In production, implement proper JWT/OAuth validation
    return token == os.getenv('API_TOKEN', 'default_secret')

# ========== PRODUCTION CONFIGURATION ==========
if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    port = int(os.getenv("FLASK_PORT", "5000"))
    
    if debug_mode:
        logger.warning("Running in DEVELOPMENT mode")
        app.run(host="0.0.0.0", port=port, debug=debug_mode)
    else:
        logger.info("Starting PRODUCTION server")
        from waitress import serve
        serve(app, host="0.0.0.0", port=port)

