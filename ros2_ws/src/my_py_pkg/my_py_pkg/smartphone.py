#!/usr/bin/env python3
#all these dependencies (imports of other ros packages) need to be added to the package.xml file
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String 

class SmartPhoneNode(Node):
    def __init__(self):
        super().__init__("smartphone")
        #create subscriber
        self.subscriber_=self.create_subscription(msg_type=String, 
                                                  topic="robot_news_topic",
                                                  callback=self.callback_robot_news,   #each time the topic updates with a msg, the callback is executed
                                                  qos_profile=10)


        self.get_logger().info("Smartphone subscriber has started.")

    def callback_robot_news(self,msg):      #the msg is from the topic subscribed to 
        self.get_logger().info(msg.data)

def main(args=None):
    #first line to write in each ROS2 program. Initialize ROS2 communications
    rclpy.init(args=args)

    #create node 
    node=SmartPhoneNode()

    #Pause the program and allow the node to be alive
    rclpy.spin(node)

    #last line of program
    rclpy.shutdown()

if __name__=="__main_":
    main()