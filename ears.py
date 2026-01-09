#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# TODO: Import OpenWakeWord and Whisper libraries here
# import openwakeword
# import whisper

class EarsNode(Node):
    def __init__(self):
        super().__init__('ears_node')
        self.publisher_ = self.create_publisher(String, '/human_speech', 10)
        
        # Timer to check for audio (simulating a loop)
        # In production, you might want a separate thread for blocking audio I/O
        self.timer = self.create_timer(0.1, self.audio_loop)
        
        self.get_logger().info('👂 Ears Node Started. Listening for wake word...')

    def audio_loop(self):
        # 1. Listen to Microphone Buffer
        # audio_data = mic.read()

        # 2. Check Wake Word
        # if wake_word_engine.predict(audio_data):
        #     self.get_logger().info('Wake word detected! Recording...')
        #     recorded_audio = self.record_until_silence()
        #     text = self.transcribe(recorded_audio)
        #     self.publish_speech(text)
        pass

    def publish_speech(self, text):
        msg = String()
        msg.data = text
        self.publisher_.publish(msg)
        self.get_logger().info(f'🗣️  Heard: "{text}"')

def main(args=None):
    rclpy.init(args=args)
    node = EarsNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()