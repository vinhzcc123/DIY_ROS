from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    add_two_ints_server_node = Node(
        package= "ros2_demo_py",
        executable= "add_two_ints_server"
    )

    add_two_ints_client_node = Node(
        package= "ros2_demo_cpp",
        executable= "add_two_ints_client"
    )

    ld.add_action(add_two_ints_server_node)
    ld.add_action(add_two_ints_client_node)
    return ld