# edge_command_server.py
from flask import Flask, jsonify
from drone_control.drone_control import start_mission

app = Flask(__name__)

@app.route('/start_mission', methods=['POST'])
def trigger_mission():
    """
    This endpoint triggers the drone mission.
    In a full integration, this would be triggered by sensor readings.
    For now, you can simulate the trigger with a simple HTTP POST.
    """
    result = start_mission()
    if "failed" in result:
        return jsonify({"status": "error", "message": result}), 500
    return jsonify({"status": "success", "message": result}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=Tr
    ue)
