from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='bucky_voice',
            executable='ears.py',
            name='ears',
            output='screen'
        ),
        Node(
            package='bucky_voice',
            executable='brain.py',
            name='brain',
            output='screen'
        ),
        Node(
            package='bucky_voice',
            executable='commander.py',
            name='commander',
            output='screen'
        ),
    ])