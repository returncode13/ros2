#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("py_test")
        self.counter_=0
        self.get_logger().info("Hello OOP World! ROS2")
        self.create_timer(0.5, self.timer_callback)    #call callback_fn every 0.5 secs

    def timer_callback(self):
        self.counter_+=1
        self.get_logger().info("Timer Hello " + str(self.counter_))

def main(args=None):
    #first line to write in each ROS2 program. Initialize ROS2 communications
    rclpy.init(args=args)        

    #create node 
    node=MyNode()

    #Pause the program and allow the node to be alive
    rclpy.spin(node)                  #callbacks etc are called from the spin function.
                                      #Publishers/Subscribers go here.


    #last line of program
    rclpy.shutdown()

if __name__ == "__main__":
    main()