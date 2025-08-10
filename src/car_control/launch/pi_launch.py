from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # USB camera node
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_cam',
            parameters=[{
                'video_device': '/dev/video4',  # adjust as needed
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
        # Image viewer node
        '''
        Node(
            package='car_control',
            executable='image_viewer',
            name='image_viewer',
            output='screen',
        ),
   	'''
    ])

