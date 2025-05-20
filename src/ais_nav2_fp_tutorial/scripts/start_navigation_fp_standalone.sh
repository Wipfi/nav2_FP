#!/bin/bash
set -e


# Kill existing tmux session if it exists
if tmux has-session -t navigation_base 2>/dev/null; then
    echo ">> Existing tmux session 'navigation_base' found. Killing it..."
    tmux kill-session -t navigation_base
    sleep 2
fi


echo ">> Starting Navigation Base"

tmux new-session -d -s navigation_base

# Create new window for navigation
tmux new-window -t navigation_base -n navigation

# Split into 4 panes
tmux select-window -t navigation_base:navigation
tmux split-window -h            # split horizontally into left/right
tmux split-window -v            # split bottom right into top/bottom
tmux select-pane -t 0
tmux split-window -v            # split bottom left into top/bottom

# Now you have 4 panes: 0, 1, 2, 3
# You can send commands to each pane like this:
tmux send-keys -t navigation_base:navigation.0 "source /opt/ros/humble/setup.bash && source /home/robolab/ros2_navigation_ws/install/setup.bash && ros2 launch ais_nav2_fp_tutorial fp_driver_node.launch" C-m
tmux send-keys -t navigation_base:navigation.1 "source /opt/ros/humble/setup.bash && source /home/robolab/ros2_navigation_ws/install/setup.bash && ros2 launch ais_nav2_fp_tutorial navsat_transform.launch.py" C-m 
tmux send-keys -t navigation_base:navigation.2 "source /opt/ros/humble/setup.bash && source /home/robolab/ros2_navigation_ws/install/setup.bash && ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 vrtk_link base_link" C-m
tmux send-keys -t navigation_base:navigation.3 "source /opt/ros/humble/setup.bash && source /home/robolab/ros2_navigation_ws/install/setup.bash && ros2 launch ais_nav2_fp_tutorial gps_waypoint_follower.launch.py" C-m

echo "Robot started, attach with 'tmux attach-session -t navigation_base'" 

