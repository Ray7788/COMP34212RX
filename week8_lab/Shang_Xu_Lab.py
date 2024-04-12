from naoqi import ALProxy
import math
# This lab is written by Shang Xu and it is successfully ran on pepper robot.
def walk_back_and_forth(ip, port):
    # Create a proxy to the motion service
    motion = ALProxy("ALMotion")
    
    # Wake up robot
    motion.wakeUp()
    
    # Define the walking parameters
    x_forward = 0.5  # forward 50 cm
    x_backward = -0.5  # backward 50 cm
    y = 0.0  # no lateral movement
    theta = 0.0  # no rotation

    # Walk forward
    motion.moveTo(x_forward, y, theta)
    
    # Walk backward
    motion.moveTo(x_backward, y, theta)
    
    # Go to rest after motion
    motion.rest()


def walk_and_turn_back(ip, port):
    # Create a proxy to the motion service
    motion = ALProxy("ALMotion")
    
    # Wake up robot
    motion.wakeUp()
    
    # Define the walking and rotation parameters
    x_forward = 0.5  # forward 50 cm
    y = 0.0  # no lateral movement
    theta_180 = 3.14159  # 180 degrees in radians

    # Walk forward
    motion.moveTo(x_forward, y, 0)  # Move forward 50 cm

    # Rotate 180 degrees
    motion.moveTo(0, y, theta_180)

    # Walk forward to return to the starting position
    motion.moveTo(x_forward, y, 0)
    
    # Go to rest after motion
    motion.rest()
    

def navigate_grid(ip, port, start, end):
    # Create a proxy to the motion service
    motion = ALProxy("ALMotion")

    # Wake up the robot
    motion.wakeUp()
    
    # Calculate differences in the grid coordinates
    dx = (end[0] - start[0]) * 0.5  # Difference in x, multiplied by cell length
    dy = (end[1] - start[1]) * 0.5  # Difference in y, multiplied by cell length

    # Calculate the angle to turn using atan2
    theta = math.atan2(dy, dx)

    # Distance to travel
    distance = math.sqrt(dx**2 + dy**2)

    # First, turn to the correct direction
    motion.moveTo(0, 0, theta)

    # Then, move forward the calculated distance
    motion.moveTo(distance, 0, 0)
    
    # Go to rest after motion
    motion.rest()
    

# Replace '192.168.1.1' with the IP address of your Pepper robot
# Replace 9559 with the port number if different
walk_back_and_forth("192.168.1.1", 9559)

# Replace '192.168.1.1' with the IP address of your Pepper robot
# Replace 9559 with the port number if different
walk_and_turn_back("192.168.1.1", 9559)

# Example usage:
# Replace '192.168.1.1' with the IP address of your Pepper robot
# Replace 9559 with the port number if different
navigate_grid("192.168.1.1", 9559, (0, 0), (3, 0))
navigate_grid("192.168.1.1", 9559, (3, 0), (0, 3))
navigate_grid("192.168.1.1", 9559, (0, 3), (3, 3))
