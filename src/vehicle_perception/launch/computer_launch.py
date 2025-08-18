from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Path to your RViz config file
    rviz_config_file = os.path.join(
        get_package_share_directory('rplidar_ros'),
        'rviz',
        'rplidar.rviz'  # or the name of your rviz config file
    )
    return LaunchDescription([
        # Image viewer node
        Node(
            package='vehicle_perception',
            executable='image_viewer',
            name='image_viewer',
            output='screen',
        ),
                # Static transform: base_link -> laser_frame
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='laser_tf_pub',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'laser_frame']
        ),
        # RViz2 node
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_file]
        ),
    ])

