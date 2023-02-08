#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"

using std::placeholders::_1;
using std::placeholders::_2;

class AddTwoIntsClientNode: public rclcpp::Node
{
public:
    AddTwoIntsClientNode() : Node("add_two_ints_client"){
        RCLCPP_INFO(this->get_logger(), "Add two ints server has been started");

        // thread1_ = std::thread(std::bind(&AddTwoIntsClientNode::callbackAddTwoIntsServer, this, 1, 11));
        threads_.push_back(std::thread(std::bind(&AddTwoIntsClientNode::callbackAddTwoIntsServer, this, 2, 12)));
        threads_.push_back(std::thread(std::bind(&AddTwoIntsClientNode::callbackAddTwoIntsServer, this, 3, 13)));
    }

    void callbackAddTwoIntsServer(int a, int b){
        auto client = this->create_client<example_interfaces::srv::AddTwoInts>("add_two_ints");
        while (!client->wait_for_service(std::chrono::seconds(1)))
        {
            RCLCPP_WARN(this->get_logger(), "Waiting for add two ints server");
        }
        auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
        request->a = a;
        request->b = b;
        
        auto future = client->async_send_request(request);

        try{
            auto reponse = future.get();
            RCLCPP_INFO(this->get_logger(), "%d + %d = %d", request->a, b, reponse->sum);
        } catch(std::exception &e){
            RCLCPP_INFO(this->get_logger(), "Service call failed");
        }
    }

    private:
    // std::thread thread1_;
    std::vector<std::thread> threads_;
    rclcpp::TimerBase::SharedPtr timer_;
    std::string robot_name_;
    int counter_;
};


int main(int argc, char **argv){
    rclcpp::init(argc, argv);
    auto node = std::make_shared<AddTwoIntsClientNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}