#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"


class RobotNewsStationNode : public rclcpp::Node 
{
  public:
    RobotNewsStationNode(): Node("robot_news_station"),robot_name_("L10")
    {
        //Create Publisher using the create_publisher call. 
        //the name of the topic is mentioned as part of the constructor call.
        publisher_ = this -> create_publisher<example_interfaces::msg::String>("robot_news_topic",10);


        //publish using the callback and timer
        timer_=this->create_wall_timer(std::chrono::milliseconds(500),
                                       std::bind(&RobotNewsStationNode::publishNews, this)
                                       );
    }

   private:

   /**
    *  callback for publishing to topic
    * 
    */
   void publishNews()
   {
       //Create msg
       auto msg=example_interfaces::msg::String();
       msg.data="Hi, this is "+this->robot_name_+std::string(" from the Robot news station!");

       //Publish
       publisher_ -> publish(msg);
   };
    
   std::string robot_name_;
   rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;
   rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char** argv)
{
    //Initialise the node
    rclcpp::init(argc,argv);

    //Create the node
    auto node = std::make_shared<RobotNewsStationNode>();
    
    //Keep the node alive
    rclcpp::spin(node);

    //Shutdown node
    rclcpp::shutdown();
    return 0;

}