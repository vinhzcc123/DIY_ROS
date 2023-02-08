#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

# create class to excute
class RobotNewsStationNode(Node):
    def __init__(self):
        self.counter_ = 0
        super().__init__("robot_news_station")

        self.robot_name_ = "C3P0"
        self.publisher_ = self.create_publisher(String, "News", 10)
        self.timer_ = self.create_timer(1, self.publisher_news)
        self.get_logger().info("This is robot news has been started")

    def publisher_news(self):
        msg = String()
        msg.data = "This is news for" + str(self.robot_name_) + " time(s) " + str(self.counter_)
        self.publisher_.publish(msg)
        self.counter_ += 1

def main(args = None):
    rclpy.init(args=args)
    node = RobotNewsStationNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()