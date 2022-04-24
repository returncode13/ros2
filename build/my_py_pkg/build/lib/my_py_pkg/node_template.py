#!/usr/bin/env python3
#all these dependencies (imports of other ros packages) need to be added to the package.xml file
import rclpy
from rclpy.node import Node

class CustomNode(Node):
    def __init__(self):
        super().__init__("Node name")


def main(args=None):
    #first line to write in each ROS2 program. Initialize ROS2 communications
    rclpy.init(args=args)

    #create node 
    node=CustomNode()

    #Pause the program and allow the node to be alive
    rclpy.spin(node)

    #last line of program
    rclpy.shutdown()

if __name__=="__main_":
    main()