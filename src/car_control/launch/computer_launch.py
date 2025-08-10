from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Image viewer node
        Node(
            package='car_control',
            executable='image_viewer',
            name='image_viewer',
            output='screen',
        ),
    ])

