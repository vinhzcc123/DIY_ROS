#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"
// #include "rclcpp/timer.hpp"

class RobotNewsStationNode: public rclcpp::Node
{
public:
    RobotNewsStationNode() : Node("robot_news_station"),
                             counter_(0),
                             robot_name_("R2D2"){
        publisher_ = this->create_publisher<example_interfaces::msg::String>("robot_news", 10);
        timer_ = this->create_wall_timer(std::chrono::seconds(1),
                                        std::bind(&RobotNewsStationNode::publish_news, this));
        RCLCPP_INFO(this->get_logger(), "Robot Station has been started");
    }

private:
    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;

    void publish_news(){
        auto msg = example_interfaces::msg::String();
        msg.data = "Robot publishes the name is "+ robot_name_ + " times " + std::to_string(counter_);
        publisher_->publish(msg);
        counter_++;
    }

    rclcpp::TimerBase::SharedPtr timer_;
    std::string robot_name_;
    int counter_;
};


int main(int argc, char **argv){
    rclcpp::init(argc, argv);
    auto node = std::make_shared<RobotNewsStationNode>();
    
    rclcpp::spin(node);

    rclcpp::shutdown();

    return 0;
}