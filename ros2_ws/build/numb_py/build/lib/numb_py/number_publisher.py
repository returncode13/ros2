#!/usr/bin/env python3
#all these dependencies (imports of other ros packages) need to be added to the package.xml file
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64    

class NumberPublisher(Node):
    def __init__(self):
        super().__init__("number_publisher")
        #create a publisher and topic
        self.publisher_ = self.create_publisher(msg_type=Int64,
                                                topic="number",
                                                qos_profile=10)
        #create a timer to callback periodically
        self.timer_=self.create_timer(1,self.publish_numbers)
        self.get_logger().info("The number publisher node has started.")
        


    def publish_numbers(self):
        msg=Int64()
        msg.data=13         
        #publish
        self.publisher_.publish(msg=msg)

def main(args=None):
    #first line to write in each ROS2 program. Initialize ROS2 communications
    rclpy.init(args=args)

    #create node 
    node=NumberPublisher()

    #Pause the program and allow the node to be alive
    rclpy.spin(node)

    #last line of program
    rclpy.shutdown()

if __name__=="__main_":
    main()