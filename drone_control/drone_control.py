import socket
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("DroneControl")

# Tello connection parameters
TELLO_IP = "192.168.10.1"
TELLO_PORT = 8889
LOCAL_PORT = 9000

# Set up UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", LOCAL_PORT))
sock.settimeout(5)

def send_command(command: str, delay: int = 3) -> str:
    """Sends command to Tello drone with enhanced error handling"""
    logger.info(f"Sending command: {command}")
    try:
        sock.sendto(command.encode("utf-8"), (TELLO_IP, TELLO_PORT))
        time.sleep(delay)
        response, _ = sock.recvfrom(1024)
        decoded_response = response.decode("utf-8")
        logger.info(f"Received response: {decoded_response}")
        return decoded_response
    except (socket.timeout, ConnectionResetError) as e:
        logger.error(f"Drone communication failure: {str(e)}")
        return "error"
    except Exception as e:
        logger.critical(f"Unexpected error: {str(e)}")
        return "critical_error"

def start_mission():
    """Executes cleaning mission sequence with robust error handling"""
    try:
        # Command mode
        if send_command("command") != "ok":
            logger.error("Failed to enter command mode")
            return "command_mode_failure"

        # Takeoff (using a longer delay for a proper response)
        if send_command("takeoff", delay=5) != "ok":
            logger.error("Takeoff failed")
            return "takeoff_failure"

        logger.info("Cleaning mission in progress...")
        time.sleep(10)

        # Landing
        if send_command("land", delay=5) != "ok":
            logger.error("Landing failed")
            return "landing_failure"

        return "mission_success"
    except Exception as e:
        logger.critical(f"Mission sequence failed: {str(e)}")
        return "sequence_failure"
