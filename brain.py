#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from bucky_voice.msg import RobotIntent
import json

class BrainNode(Node):
    def __init__(self):
        super().__init__('brain_node')
        self.subscription = self.create_subscription(
            String,
            '/human_speech',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(RobotIntent, '/robot_intent', 10)
        self.get_logger().info('🧠 Brain Node Started. Waiting for speech...')

    def listener_callback(self, msg):
        command_text = msg.data.lower()
        self.get_logger().info(f'Processing: "{command_text}"')
        
        intent = self.extract_intent(command_text)
        if intent:
            self.publisher_.publish(intent)
            self.get_logger().info(f'🚀 Published Intent: {intent.action} {intent.target}')

    def extract_intent(self, text):
        msg = RobotIntent()
        
        # --- Option 1: Hard-Coded Approach ---
        if "pick" in text or "grab" in text:
            msg.action = "PICK"
            if "red" in text:
                msg.color = "RED"
            if "screwdriver" in text:
                msg.target = "SCREWDRIVER"
            return msg

        # --- Option 2: LLM Approach (Placeholder) ---
        # prompt = f"Convert to JSON: {text}"
        # response = llm_client.generate(prompt)
        # data = json.loads(response)
        # msg.action = data.get('action', '').upper()
        # msg.target = data.get('target', '').upper()
        # msg.coordinate_offset = data.get('coordinate_offset', [0.0, 0.0, 0.0])
        # return msg

        self.get_logger().warn("Could not understand intent.")
        return None

def main(args=None):
    rclpy.init(args=args)
    node = BrainNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()