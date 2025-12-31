# Bucky Robot Arm - ROS 2 Setup

## Project Structure

```
bucky_description/  - Robot model (URDF, meshes, visual files)
bucky_bringup/     - Launch files to start the robot
```

# Next Steps

insert XACRO in `bucky_description/urdf/bucky.urdf.xacro`

Use [sw_urdf_exporter](http://wiki.ros.org/sw_urdf_exporter)

After conversion:
1. Place your URDF/XACRO files in `bucky_description/urdf/`
2. Place mesh files (STL/DAE) in `bucky_description/meshes/`
3. Update the filename in launch file if different from `bucky.urdf.xacro`

### 2. Testing with Foxglove Studio

Terminal 1 - Start the robot:**
```bash
cd ~/ros2_ws
source /opt/ros/kilted/setup.bash
source install/setup.bash
ros2 launch bucky_bringup display.launch.py
```

This will:
- Publish the robot description
- Start Joint State Publisher GUI (to move joints manually)
- Broadcast TF transforms

Terminal 2 - Start Foxglove Bridge:**
```bash
source /opt/ros/kilted/setup.bash
ros2 launch foxglove_bridge foxglove_bridge_launch.xml
```

Connect to Foxglove
Connect to `ws://localhost:8765`
Add a 3D panel and subscribe to `/robot_description` topic

I have added joint sliders

### 4. Next up

Once you can visualize your robot:

**For Simulation:**
- Add Gazebo simulation with physics and controllers
- Configure ros2_control for joint control

**For Real Hardware:**
- Set up hardware interface for your motor controllers
- Configure ros2_control with your specific hardware

**For Motion Planning:**
- Set up MoveIt2 for trajectory planning
- Add collision checking and inverse kinematics