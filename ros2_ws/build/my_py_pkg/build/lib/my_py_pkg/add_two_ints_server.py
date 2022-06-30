#!/usr/bin/env python3
#all these dependencies (imports of other ros packages) need to be added to the package.xml file
import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

class AddTwoIntsServerNode(Node):
    def __init__(self):
        super().__init__("add_two_ints_server")
        self.server_=self.create_service(
                                            AddTwoInts,
                                            "add_two_ints",
                                            self.callback_add_two_ints)
        self.get_logger().info("add_two_ints_server started.")

    def callback_add_two_ints(self,request,response):
        #first check the output of ros interface show example_interfaces/srv/AddTwoInts
        #
        response.sum=request.a+request.b
        self.get_logger().info(str(request.a) + "+" +str(request.b)+" = "+str(response.sum))
        return response


def main(args=None):
    #first line to write in each ROS2 program. Initialize ROS2 communications
    rclpy.init(args=args)

    #create node 
    node=AddTwoIntsServerNode()

    #Pause the program and allow the node to be alive
    rclpy.spin(node)

    #last line of program
    rclpy.shutdown()

if __name__=="__main_":
    main()