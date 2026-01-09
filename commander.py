#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from bucky_voice.msg import RobotIntent

# TODO: Import MoveIt bindings
# from moveit_commander import MoveGroupCommander

class CommanderNode(Node):
    def __init__(self):
        super().__init__('commander_node')
        self.subscription = self.create_subscription(
            RobotIntent,
            '/robot_intent',
            self.intent_callback,
            10)
        
        self.get_logger().info('🤖 Commander Node Started. Ready to move Bucky.')
        
        # Initialize MoveIt (Placeholder)
        # self.arm_group = MoveGroupCommander("bucky_arm")
        # self.gripper_group = MoveGroupCommander("gripper")

    def intent_callback(self, msg):
        self.get_logger().info(f'Received Command: {msg.action} -> {msg.color} {msg.target}')
        
        if msg.action == "PICK":
            self.execute_pick(msg.target, msg.color)
        else:
            self.get_logger().warn(f"Unknown action: {msg.action}")

    def execute_pick(self, target, color):
        # 1. Look up coordinates (TF/Vision)
        # 2. Plan path with MoveIt
        # 3. Execute
        # 4. Close Gripper
        self.get_logger().info(f"Executing sequence: Picking up {color} {target}...")

def main(args=None):
    rclpy.init(args=args)
    node = CommanderNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()