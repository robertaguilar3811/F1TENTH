from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():

    # Path to your RViz config file
    rviz_config_file = os.path.join(
        os.path.expanduser('~'),
        'Documents/F1TENTH/src/vehicle_perception/rviz/rplidar.rviz'
    )

    return LaunchDescription([
        # RPLidar node
        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            name='rplidar_a1',
            parameters=[{
                'serial_port': '/dev/ttyUSB0',   # change to /dev/ttyACM0 if needed
                'serial_baudrate': 115200,       # sometimes 256000 is needed
                'frame_id': 'laser_frame',
                'inverted': False,
                'angle_compensate': True,
                'scan_mode': 'Sensitivity'
            }]
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
