#include "rclcpp/rclcpp.hpp"
// #include "rclcpp/timer.hpp"

class Node_Demo: public rclcpp::Node
{
public:
    Node_Demo() : Node("demo_node_test"),
                  counter_(0){
        RCLCPP_INFO(this->get_logger(), "Hello from Vinh");
        timer = this->create_wall_timer(std::chrono::seconds(2),
                                        std::bind(&Node_Demo::timer_callback, this));
    }

private:
    void timer_callback(){
        RCLCPP_INFO(this->get_logger(), "TIMES %d", counter_);
        counter_++;
    }

    rclcpp::TimerBase::SharedPtr timer;
    int counter_;
};


int main(int argc, char **argv){
    rclcpp::init(argc, argv);
    auto node = std::make_shared<Node_Demo>();
    
    rclcpp::spin(node);

    rclcpp::shutdown();
}