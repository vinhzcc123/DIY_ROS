#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# create class to excute
class _Node(Node):
    def __init__(self):
        super().__init__("first_test_node")
        self.counter_ = 0
        self.get_logger().info("Hello from Vinh, this is the first test and hello Ros 2")
        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("TIMES " + str(self.counter_))

def main(args = None):
    rclpy.init(args=args)
    node = _Node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()