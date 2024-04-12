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

    # Disconnect from the Pepper robot
    robot.__del__()
