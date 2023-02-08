#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

# create class to excute
class SmartPhoneNode(Node):
    def __init__(self):
        self.counter_ = 0
        super().__init__("smartphone")

        self.get_logger().info("SmartPhone has been started")
        self.subcriber_ = self.create_subscription(String, "News", 
                                                   self.message_callback, 10)

    def message_callback(self, msg):
        self.get_logger().info(msg.data)

def main(args = None):
    rclpy.init(args=args)
    node = SmartPhoneNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()