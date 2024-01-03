import os
from pathlib import Path

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.actions import DeclareLaunchArgument, TimerAction
from launch.conditions import IfCondition, UnlessCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_quadruped = get_package_share_directory('quadruped_description')
    urdf_file = Path(pkg_quadruped) / 'urdf/quadruped.urdf'
    configs = Path(pkg_quadruped) / 'config'
    world_file = Path(pkg_quadruped) / 'simulation/worlds/quadruped.world'
    
    sim = LaunchConfiguration('sim', default='false')

    # Gazebo launch
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')),
        condition=IfCondition(LaunchConfiguration('sim'))
    )

    rviz = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', str(configs/ 'quadruped.rviz')],
        condition=IfCondition(LaunchConfiguration('rviz'))
    )


    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        namespace="quadruped",
        name="quadruped_rsp",
        output='screen',
        parameters=[{"use_sim_time" : sim}],
        arguments=[str(urdf_file)])

    return LaunchDescription([
    	DeclareLaunchArgument('sim', default_value='true', description='Run stack in simulation.'),
        DeclareLaunchArgument('world', default_value=str(world_file), description='Simulation world file'),
        DeclareLaunchArgument('rviz', default_value='false', description='Open RViz.'),
        gazebo,
        robot_state_publisher,
        TimerAction(period=5.0, actions=[rviz])
    ])
