from naoqi import ALProxy

def connect_to_robot(robot_ip, port):
    """
    Connects to the Pepper robot with the given IP address and port.
    Returns an ALMotion proxy object for controlling the robot's motion.
    """
    try:
        motion_proxy = ALProxy("ALMotion", robot_ip, port)
        return motion_proxy
    except Exception as e:
        print("Error while connecting to the robot:", e)
        return None

def walk_forward(robot, distance):
    """
    Makes the Pepper robot walk forward for the specified distance (in meters).
    """
    # Set the speed of the robot (meters per second)
    robot.setWalkTargetVelocity(0.5, 0, 0)  # Adjust the speed as needed

    # Move the robot forward
    robot.moveTo(distance, 0, 0)

def walk_backward(robot, distance):
    """
    Makes the Pepper robot walk backward for the specified distance (in meters).
    """
    # Set the speed of the robot (meters per second)
    robot.setWalkTargetVelocity(-0.5, 0, 0)  # Adjust the speed as needed

    # Move the robot backward
    robot.moveTo(-distance, 0, 0)

def rotate(robot, angle):
    """
    Rotates the Pepper robot in place by the specified angle (in degrees).
    """
    # Set the speed of the robot (radians per second)
    robot.setWalkTargetVelocity(0, 0, 0.5)  # Adjust the speed as needed

    # Rotate the robot
    robot.moveTo(0, 0, angle)

import math

# Grid cell length
l = 0.5

def calculate_direction(start, end):
    """
    Calculate the direction (in degrees) from start to end.
    """
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    return math.degrees(math.atan2(dy, dx))

def move_to_target(start, end):
    """
    Move the robot from the start position to the end position.
    """
    # Calculate direction to the target
    direction = calculate_direction(start, end)
    
    # Rotate the robot to face the target direction
    rotate(robot, direction)
    
    # Calculate the distance to the target
    distance = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2) * l
    
    # Move the robot forward to the target
    walk_forward(robot, distance)

if __name__ == "__main__":
    # Set the IP address and port of the Pepper robot
    robot_ip = "<robot_ip>"
    port = <port_number>

    # Connect to the Pepper robot
    robot = connect_to_robot(robot_ip, port)
    if robot is None:
        exit()

    # Example usage: Walk forward for 50 cm
    walk_forward(robot, 0.5)

    # Example usage: Stop
    robot.stopMove()

    # Example usage: Walk backward for 50 cm
    walk_backward(robot, 0.5)

    # Example usage: Rotate 180 degrees
    rotate(robot, 180)

# -------------------
    # Set the coordinates of the starting and ending positions
    start = (1, 1)  # Example starting position
    end = (3, 3)    # Example ending position

    # Move the robot from the starting position to the ending position
    move_to_target(start, end)
# ---

    # Disconnect from the Pepper robot
    robot.__del__()
