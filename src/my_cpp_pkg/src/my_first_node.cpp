#include "rclcpp/rclcpp.hpp"

class MyNode: public rclcpp::Node
{
    public:
        MyNode():Node("cpp_test"),counter_(0)
        {
            //print some info
            RCLCPP_INFO(this->get_logger(),"Hello OOP Cpp World!");

            timer_=this->create_wall_timer(std::chrono::seconds(1),                     //time interval
                                           std::bind(&MyNode::timerCallback, this));    //std::bind needed for calling callback
        }

    private:

        void timerCallback()
        {
            counter_++;
            RCLCPP_INFO(this->get_logger(),"Timer Hello %d",counter_);
        }
        
        //shared pointer to a timer
        rclcpp::TimerBase::SharedPtr timer_;
        int counter_;
};

int main(int argc, char** argv)
{
    //first line to write in each ROS2 program. Initialize ROS2 communications
    rclcpp::init(argc,argv);

    //create node
    auto node=std::make_shared<MyNode>();                  //auto is shared pointer. make_shared returns shared_pointer
                                                           //no need to new and delete
    
    
    //spin the node. keep it alive
    rclcpp::spin(node);

    //last part of the program
    rclcpp::shutdown();

    return 0;


}
