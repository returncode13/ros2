#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"
using namespace std;

class Number_Counter : public rclcpp::Node //Modify Name
{
  public:
    Number_Counter(): Node("number_counter"),counter_(0)  //Modify Name
    {
        //This node is a subscriber
        subscriber_=this->create_subscription<example_interfaces::msg::Int64>(
            "number",     //topic to read from
            10,
            std::bind(&Number_Counter::readFromTopic,this,std::placeholders::_1)
        );
        
        //This node is a publisher
        publisher_=this->create_publisher<example_interfaces::msg::Int64>(
            "number_count",   //topic to write to
            10
        );

        //timer to publish 
        timer_=this->create_wall_timer(std::chrono::milliseconds(1000),
                                      std::bind(&Number_Counter::incrementCounter,this)
                                      );
    }

   private:
   rclcpp::Subscription<example_interfaces::msg::Int64>::SharedPtr subscriber_;
   rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher_;
   rclcpp::TimerBase::SharedPtr timer_;
   int64_t counter_;

   //subscriber Callback
   void readFromTopic(const example_interfaces::msg::Int64::SharedPtr message)
   {
        auto s=std::to_string(message->data);
        s="Subscriber: "+s;
        RCLCPP_INFO(this->get_logger(),s); 
   };

   //publisher callback
   void incrementCounter()
   {   
       auto msg=example_interfaces::msg::Int64();
       msg.data=counter_;

       //publish
       publisher_ -> publish(msg); 
       counter_+=1;
   };
};

int main(int argc, char** argv)
{
    //Initialise the node
    rclcpp::init(argc,argv);

    //Create the node
    auto node = std::make_shared<Number_Counter>();
    
    //Keep the node alive
    rclcpp::spin(node);

    //Shutdown node
    rclcpp::shutdown();
    return 0;

}