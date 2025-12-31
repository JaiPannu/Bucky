# Bucky Setup

## Project Structure

```
bucky_description/  - Robot model (URDF, meshes, visual files)
bucky_bringup/     - Launch files to start the robot
```

# Next steps

Connect to Foxglove
Connect to `ws://localhost:8765`
Add a 3D panel and subscribe to `/robot_description` topic

I have added joint sliders

Next up

Once you can visualize your robot:

For Simulation:
- Add Gazebo simulation with physics and controllers
- Configure ros2_control for joint control

For Real Hardware:
- Set up hardware interface for your motor controllers
- Configure ros2_control with your specific hardware

For Motion Planning:
- Set up MoveIt2 for trajectory planning
- Add collision checking and inverse kinematics