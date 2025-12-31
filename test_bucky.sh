#!/bin/bash

# Quick test script for Bucky robot arm visualization

echo "🤖 Starting Bucky Robot Arm..."
echo ""
echo "This will launch:"
echo "  - Robot State Publisher (publishes robot model)"
echo "  - Joint State Publisher GUI (control joint positions)"
echo ""
echo "To visualize in Foxglove:"
echo "  1. Install Foxglove Studio from https://foxglove.dev/download"
echo "  2. In another terminal, run: ros2 launch foxglove_bridge foxglove_bridge_launch.xml"
echo "  3. Open Foxglove and connect to ws://localhost:8765"
echo "  4. Add a 3D panel and you'll see Bucky!"
echo ""
echo "Starting in 3 seconds..."
sleep 3

cd ~/ros2_ws
source /opt/ros/kilted/setup.bash
source install/setup.bash

ros2 launch bucky_bringup display.launch.py
#Ai written test