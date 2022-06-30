#!/usr/bin/env python3
import re
from urllib import request, response
import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

def main(args=None):
    rclpy.init(args=args)
    node=Node("add_two_ints_no_oop")

    client=node.create_client(AddTwoInts,"add_two_ints")         #address an already existing service called "add_two_ints"

    #warn if the server isn't found
    while not client.wait_for_service(1.0):
        node.get_logger().warn("Waiting for service add_two_ints ...")

    request=AddTwoInts.Request()
    request.a=13
    request.b=26

    future=client.call_async(request=request)
    rclpy.spin_until_future_complete(node=node,future=future)

    try:
        response=future.result()
        node.get_logger().info(str(request.a) + "+" +str(request.b)+" = "+str(response.sum))
    except Exception as e:
        node.get_logger().error("Error %r"%(e,))

    rclpy.shutdown()

if __name__ == "__main__":
    main()