#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial

# create class to excute
class AddTwoIntClientNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.get_logger().info("Hello from Vinh, this is the first test and hello Ros 2")
        self.call_add_two_int_server(111, 222)
        self.call_add_two_int_server(112, 222)
        self.call_add_two_int_server(113, 222)

    def call_add_two_int_server(self, a, b):
        client = self.create_client(AddTwoInts, "add_two_ints")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("waiting for server")

        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        future = client.call_async(request)
        future.add_done_callback(partial(self.add_two_ints_callback, a = a, b = b))

    def add_two_ints_callback(self, future, a, b):
        try:
            reponse = future.result()
            self.get_logger().info(str(a) + " + " + str(b) + 
                                    " = " + str(reponse.sum))
        except Exception as e:
            self.get_logger().error("Service call failed %r" %(e, ))

def main(args = None):
    rclpy.init(args=args)
    node = AddTwoIntClientNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()