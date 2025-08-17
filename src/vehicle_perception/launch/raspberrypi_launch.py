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
        # USB camera node
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_cam',
            parameters=[{
                'video_device': '/dev/video0',  # adjust as needed
                'frame_id': 'camera',
                'pixel_format': 'yuyv',
                'io_method': 'mmap',
                'camera_info_url': '',
                'frame_rate': 30,
                'image_width': 640,
                'image_height': 480,
            }],
            output='screen'
        ),
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