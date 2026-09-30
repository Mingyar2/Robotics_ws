from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1. Nodo del simulador de la tortuga
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            output='screen'
        ),
        # 2. Nodo que lee el Joystick físico
        Node(
            package='basics',
            executable='joystick_pub', 
            output='screen'
        ),
        # 3. Nodo que procesa los datos y mueve la tortuga
        Node(
            package='basics',
            executable='turtle_controller',
            output='screen'
        )
    ])