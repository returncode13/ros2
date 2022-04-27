#include "rclcpp/rclcpp.hpp"

class CustomNode : public rclcpp::Node //Modify Name
{
  public:
    CustomNode(): Node("node_name")  //Modify Name
    {

    }

   private:
};

int main(int argc, char** argv)
{
    //Initialise the node
    rclcpp::init(argc,argv);

    //Create the node
    auto node = std::make_shared<CustomNode>();
    
    //Keep the node alive
    rclcpp::spin(node);

    //Shutdown node
    rclcpp::shutdown();
    return 0;

}