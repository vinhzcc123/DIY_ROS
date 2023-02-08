import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger

class FaceDetectClientNode(Node):
    def __init__(self):
        super().__init__("faces_detect_client")
        self.timer_ = self.create_timer(0.5, self.call_client)
        # self.subscriber_ = self.create_subscription(Int32, "count_faces", self.print_callback)
    def call_client(self):
        client_ = self.create_client(Trigger, "face_detect")
        while not client_.wait_for_service(1.0):
            self.get_logger().warn("waiting for server")
        request = Trigger.Request()
        future = client_.call_async(request)
        future.add_done_callback(self.print_callback)
    def print_callback(self, future):
        try:
            reponse = future.result()
            self.get_logger().info(str(reponse.success))
        except Exception as e:
            self.get_logger().error("Service call failed %r" %(e, ))

def main(args = None):
    rclpy.init(args=args)
    node = FaceDetectClientNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()