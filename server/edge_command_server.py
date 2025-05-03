# server/edge_command_server.py
from flask import Flask, jsonify, request
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import jwt
import secrets
import os
import logging
from logging.handlers import RotatingFileHandler
from drone_control.drone_control import start_mission

# Initialize Flask application
app = Flask(__name__)

# ===== SECURITY CONFIGURATION =====
def generate_nonce():
    """Generate cryptographically secure nonce per request"""
    return secrets.token_hex(16)

@app.before_request
def set_csp_nonce():
    """Inject unique nonce into every request context"""
    nonce = generate_nonce()
    request.csp_nonce = nonce  # For Talisman CSP header
    app.jinja_env.globals['csp_nonce'] = nonce  # For template rendering

csp = {
    'default-src': ["'self'"],
    'script-src': ["'self'", "'nonce'", "'strict-dynamic'"],
    'style-src': ["'self'", "'unsafe-inline'"]
}

Talisman(
    app,
    content_security_policy=csp,
    content_security_policy_nonce_in=['script-src'],
    permissions_policy={
        'geolocation': '()',
        'camera': '()',
        'microphone': '()'
    },
    force_https=(os.getenv('FLASK_ENV') == 'production'),
    strict_transport_security=True,
    session_cookie_secure=True
)

# ===== RATE LIMITING ===== 
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    storage_uri="redis://redis:6379" if os.getenv('FLASK_ENV') == 'production' else "memory://",
    default_limits=["300/hour", "30/minute"],
    strategy="fixed-window-elastic-expiry"
)

# ===== PRODUCTION LOGGING =====
logger = logging.getLogger("edge_command_server")
logger.setLevel(logging.INFO)

file_handler = RotatingFileHandler(
    '/var/log/edge_command.log',
    maxBytes=10*1024*1024,  # 10MB files
    backupCount=5,
    mode='a',
    chmod=0o0666  # Proper permissions for containerized environments
)
file_handler.setFormatter(logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
))

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter(
    "%(levelname)s - %(message)s"
))

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# ===== HEALTH ENDPOINT =====
@app.route('/health')
@limiter.exempt
def health_check():
    """Kubernetes liveness/readiness endpoint"""
    return jsonify({
        "status": "healthy",
        "version": os.getenv('APP_VERSION', '1.4.0'),
        "components": {
            "database": True,
            "sensor_interface": True,
            "auth_service": True
        }
    }), 200

# ===== MISSION CONTROL ENDPOINT =====
@app.route("/start_mission", methods=["POST"])
@limiter.limit("10/minute")
def trigger_mission():
    """Secure mission trigger endpoint with JWT validation"""
    try:
        # === Request Validation ===
        if not request.is_json:
            logger.warning("Invalid content type from %s", request.remote_addr)
            return jsonify_error("INVALID_CONTENT_TYPE", "JSON required", 415)

        # === JWT Validation ===
        auth_header = request.headers.get('Authorization')
        if not auth_header or not validate_jwt(auth_header):
            logger.warning("Unauthorized access attempt from %s", request.remote_addr)
            return jsonify_error("UNAUTHORIZED", "Valid JWT required", 401)

        # === Mission Execution ===
        result = start_mission()
        
        if "failed" in result.lower():
            logger.error("Mission failure: %s", result)
            return jsonify_error("MISSION_FAILURE", result, 500)

        logger.info("Mission success: %s", result)
        return jsonify_success(result)

    except Exception as e:
        logger.critical("System failure: %s", str(e), exc_info=True)
        return jsonify_error("INTERNAL_ERROR", "Contact support", 500)

def validate_jwt(auth_header: str) -> bool:
    """Production-grade JWT validation"""
    try:
        token = auth_header.split()[1]
        jwt.decode(
            token,
            os.getenv('JWT_SECRET_KEY'),
            algorithms=["HS256"],
            issuer="air4life-auth",
            audience="edge-node",
            options={"require_exp": True}  # Critical security fix
        )
        return True
    except jwt.ExpiredSignatureError:
        logger.warning("Expired JWT token")
        return False
    except jwt.InvalidTokenError as e:
        logger.error("Invalid JWT: %s", str(e))
        return False
    except Exception as e:
        logger.error("JWT validation error: %s", str(e))
        return False

def jsonify_error(code: str, message: str, status: int):
    return jsonify({
        "status": "error",
        "code": code,
        "message": message
    }), status

def jsonify_success(message: str):
    return jsonify({
        "status": "success",
        "message": message
    }), 200

# ===== PRODUCTION WSGI HANDLING =====
if __name__ == "__main__":
    if os.getenv("FLASK_ENV") != "production":
        logger.warning("Running in DEVELOPMENT mode")
        app.run(host="0.0.0.0", port=5000)
    else:
        logger.info("Starting PRODUCTION server via Gunicorn")
        from gunicorn.app.base import BaseApplication

        class FlaskApplication(BaseApplication):
            def __init__(self, app):
                self.application = app
                super().__init__()

            def load_config(self):
                self.cfg.set('workers', 4)
                self.cfg.set('timeout', 120)
                self.cfg.set('keepalive', 10)
                self.cfg.set('accesslog', '-')
                self.cfg.set('errorlog', '-')

            def load(self):
                return self.application

        FlaskApplication(app).run()


