
# 🧭 Fixposition VRTK2 Nav2 Integration (AIS Lab)

This repository is based on a fork of [fixposition/nav2_tutorial](https://github.com/fixposition/nav2_tutorial) and demonstrates the integration of the [Fixposition VRTK2](https://www.fixposition.com/vrtk2) global localization system into the ROS 2 Navigation Stack (Nav2) for **outdoor navigation** in the **AIS Lab**.

The focus is on testing different localization setups using the [Waypoint Follower demo](https://docs.nav2.org/tutorials/docs/navigation2_with_gps.html#tutorial-steps) from Nav2.

## ⚙️ Requirements

- **Ubuntu 22.04**
- **ROS 2 Humble**
- **Nav2**


## 🎯 Goal
Evaluate multiple integration strategies combining global and local localization sources:

- Use Fixposition VRTK2 as the global localization provider (e.g., in `map` frame)
- Combine with different sources of local odometry (wheel odometry, LiDAR odometry, or fused solutions)
- Enable waypoint-based autonomous navigation using Nav2


## 🛰️ Integration Scenarios

This repository showcases different integration strategies for outdoor navigation using the Fixposition VRTK2 device in combination with ROS 2 and the Nav2 Waypoint Follower demo.

| Scenario Name                  | Global Localization   | Local State Estimation                  | Description                                                                 | Status  |
|--------------------------------|-----------------------|-----------------------------------------|-----------------------------------------------------------------------------|---------|
| **FP Standalone**              | Fixposition VRTK2     | Fixposition VRTK2                       | Basic integration using only Fixposition as both localization and odometry  | ✅ Done |
| **FP + Wheel Odometry A**      | Fixposition VRTK2     | Wheel odometry input to Fixposition     | Adds wheel odometry as input to Fixposition fusion                          | 🔧 ToDo |
| **FP + Wheel Odometry B**      | Fixposition VRTK2     | Custom local estimation from wheel odom | Custom local EKF using wheel odometry, separate from Fixposition           | 🔧 ToDo |
| **FP + LiDAR Odometry A**      | Fixposition VRTK2     | LiDAR odometry (e.g., DLO, LOAM)        | LiDAR used independently for local estimation                               | 🔧 ToDo |
| **FP + LiDAR Odometry B**      | Fixposition VRTK2     | Custom EKF using LiDAR odometry         | EKF-based local estimation using LiDAR data                                 | 🔧 ToDo |
| **FP + LiDAR + Wheel Odometry**| Fixposition VRTK2     | Custom fusion of LiDAR + wheel odometry | Locally fuses LiDAR and wheel odometry; Fixposition for global pose         | 🔧 ToDo |

✅ = Implemented  🔧 = Planned/ToDo


## Usage
### Setup Workspace
1. If not already on your system: Install colcon build tool (`sudo apt install python3-colcon-common-extensions`)

2. Create Workspace folder in you home directory: (`mkdir ros2_navigation_ws && cd ros2_navigation_ws`)

3. Clone this repository into the folder 

4. `Colcon build`

### Install Dependencies


### Build


### Launch
