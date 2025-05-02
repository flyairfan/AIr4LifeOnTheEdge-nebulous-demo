# drone_control/drone_control.py
import socket
import time

# Tello connection parameters.
TELLO_IP = "192.168.10.1"
TELLO_PORT = 8889
LOCAL_PORT = 9000  # Local port to bind for responses

# Set up the UDP socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', LOCAL_PORT))
sock.settimeout(5)  # Wait up to 5 seconds for a response

def send_command(command: str, delay: int = 3) -> str:
    """
    Sends a command string to the Tello drone and returns its response.
    """
    print(f"Sending command: {command}")
    try:
        sock.sendto(command.encode("utf-8"), (TELLO_IP, TELLO_PORT))
        time.sleep(delay)
        response, _ = sock.recvfrom(1024)
        decoded_response = response.decode("utf-8")
        print(f"Received response: {decoded_response}")
        return decoded_response
    except socket.timeout:
        print("No response received from Tello.")
        return "timeout"

def start_mission():
    """
    Executes the cleaning mission by sending a sequence of Tello commands.
    Sequence:
      1. Enter command mode.
      2. Take off.
      3. Simulate the cleaning mission (a simple delay).
      4. Land.
    """
    # Step 1: Enter command mode.
    if send_command("command") != "ok":
        return "Failed to enter command mode."
    
    # Step 2: Take off.
    if send_command("takeoff", delay=5) != "ok":
        return "Takeoff failed."
    
    print("Drone is executing the cleaning mission...")
    time.sleep(10)  # Simulated mission duration
    
    # Step 3: Land.
    if send_command("land", delay=5) != "ok":
        return "Landing failed."
    
    return "Mission completed successful
      ly."
