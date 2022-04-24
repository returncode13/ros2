#!/usr/bin/env python3

#all these dependencies (imports of other ros packages) need to be added to the package.xml file

import queue
from unicodedata import name
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String            #get a msg type from the existing_interfaces package

class RobotNewsStationNode(Node):
    def __init__(self):
        super().__init__("robot_news_station")
        #createa publisher and the topic using the create_publisher call.
        self.publisher_=self.create_publisher(msg_type=String, topic="robot_news_topic",qos_profile=10)
        #create a timer to callback periodically
        self.timer_=self.create_timer(1,self.publish_news)
        self.get_logger().info("The robot news station node has started.")


    def publish_news(self):
        msg=String()
        msg.data="Hello World"     #"data" field is defined under example_interfaces/msg/String
        #publish the msg to the topic
        self.publisher_.publish(msg=msg)

def main(args=None):
    #first line to write in each ROS2 program. Initialize ROS2 communications
    rclpy.init(args=args)

    #create node 
    node=RobotNewsStationNode()

    #Pause the program and allow the node to be alive
    rclpy.spin(node)

    #last line of program
    rclpy.shutdown()

if __name__=="__main_":
    main()