from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    navsat_transform_params_file = os.path.join(get_package_share_directory("ais_nav2_fp_tutorial"), 
                                "config", "navsat_transform_config.yaml")

    return LaunchDescription([
        # Spawn Navsat transformation node
        Node(
            package="robot_localization",
            executable="navsat_transform_node",
            name="navsat_transform",
            output="screen",
            parameters=[navsat_transform_params_file],
            remappings=[
                ("imu/data", "/sensors/imu/data"),      # (Input) Message with orientation data
                ("odometry/filtered", "/localization/odometry/global"), # (Input) Robot's current position
                ("gps/fix", "/localization/odometry/llh"),  # (Input) Robot's GPS coordinates
                ("odometry/gps", "/localization/odometry/gps"),         # (Output) Robot's GPS coordinates, transformed into its world frame
                ("gps/filtered", "/localization/gps/filtered"),         # (Output) Robot’s world frame position, transformed into GPS coordinates
            ],
        ),
    ])