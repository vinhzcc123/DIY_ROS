#include "rclcpp/rclcpp.hpp"
#include "my_robot_interfaces/msg/hardware_status.hpp"

class HardwareStatusPublisherNode : public rclcpp::Node
{
public:
    HardwareStatusPublisherNode() : Node("hardware_publisher")
    {
        _pub = this->create_publisher<my_robot_interfaces::msg::HardwareStatus>("hardware_status", 10);
        timer_ = this->create_wall_timer(std::chrono::seconds(1), std::bind(&HardwareStatusPublisherNode::publishHardWareStatus, this));
        RCLCPP_INFO(this->get_logger(), "Hardware status has been started");
    }
private:
    void publishHardWareStatus(){
        auto msg = my_robot_interfaces::msg::HardwareStatus();
        msg.temperature = 14;
        msg.are_motors_ready = true;
        msg.debug_message = "It's too cold in Nghe An (Jan 17 2023)";
        _pub->publish(msg);
    }

    rclcpp::Publisher<my_robot_interfaces::msg::HardwareStatus>::SharedPtr _pub;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv){
    rclcpp::init(argc, argv);
    auto node = std::make_shared<HardwareStatusPublisherNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
}