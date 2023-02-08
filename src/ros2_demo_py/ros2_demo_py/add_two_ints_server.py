#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

# create class to excute
class AddTwoIntServerNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_server")
        self.server_ = self.create_service(AddTwoInts, "add_two_ints", self.add_two_ints_callback)
        self.counter_ = 0
        self.get_logger().info("Hello from Vinh, this is the first test and hello Ros 2")

        # self.create_timer(0.5, self.timer_callback)
    def add_two_ints_callback(self, request, reponse):
        reponse.sum = request.a + request.b
        self.get_logger().info("add two ints has been started")
        self.get_logger().info(str(reponse.sum))
        return reponse

    def timer_callback(self):
        self.counter_ += 1
        self.get_logger().info("TIMES " + str(self.counter_))

def main(args = None):
    rclpy.init(args=args)
    node = AddTwoIntServerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()