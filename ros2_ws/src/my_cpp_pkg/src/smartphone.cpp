#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"
class SmartPhoneNode : public rclcpp::Node //Modify Name
{
  public:
    SmartPhoneNode(): Node("smartphone")  //Modify Name
    {
        //Initialize the subscriber with the topic its subscribed to and the 
        //callback called when the topic updates
        subscriber_=this->create_subscription<example_interfaces::msg::String>(
            "robot_news_topic",
            10,
            std::bind(&SmartPhoneNode::readNews,this,std::placeholders::_1));
        RCLCPP_INFO(this->get_logger()," Smartphone node has started!");


    };

   private:
   rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber_;

   //Callback for reading msgs from topics
   void readNews(const example_interfaces::msg::String::SharedPtr message)
   {

       RCLCPP_INFO(this->get_logger(),message->data.c_str());
   };
};

int main(int argc, char** argv)
{
    //Initialise the node
    rclcpp::init(argc,argv);

    //Create the node
    auto node = std::make_shared<SmartPhoneNode>();
    
    //Keep the node alive
    rclcpp::spin(node);

    //Shutdown node
    rclcpp::shutdown();
    return 0;

}