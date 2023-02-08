#!/usr/bin/env python3
import rclpy
import cv2
from rclpy.node import Node
from std_msgs.msg import Int32
from std_srvs.srv import Trigger

class FaceDetectServerNode(Node):
    def __init__(self):
        self.n = 0
        super().__init__("faces_detect_server")
        self.timer_ = self.create_timer(1.0, self.publish_face_number)
        self.publisher_ = self.create_publisher(Int32, "count_faces", 10)
        self.server_ = self.create_service(Trigger, "face_detect", self.faces_detect_callback)
        self.get_logger().info("The Face Detection Node is starting")

    def faces_detect_callback(self):
        face_cascade = cv2.CascadeClassifier('../../haarcascade/haarcascade_frontalface_default.xml')
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                self.n += 1
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            self.publish_face_number()

        cap.release()
        cv2.destroyAllWindows()

    def publish_face_number(self):
        self.msg = Int32()
        self.msg.data = self.n
        self.publisher_.publish(self.msg)
    
def main(args = None):
    rclpy.init(args=args)
    node = FaceDetectServerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()