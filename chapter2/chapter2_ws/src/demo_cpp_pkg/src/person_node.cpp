#include "rclcpp/rclcpp.hpp"
using namespace std;

class PersonNode : public rclcpp::Node // 继承rclcpp类别的Node节点
{
private:
    std::string name;
    int age;

public:
    PersonNode(const string &node_name, const string &name, const int &age)
        : Node(node_name) // 调用父类的构造函数
    // 类似于python中super().__init__(node_name)
    {
        this->name = name;
        this->age = age;
    };
    void eat(const string &food_name)
    {
        // cout<<"姓名："<<endl;
        RCLCPP_INFO(this->get_logger(), "我是%s,%d岁,爱吃%s", name.c_str(), age, food_name.c_str());
    }
};
int main(int argc,char ** argv)//程序入口参数
{
    // cout<<"参数变量"<<argc<<endl;
    // cout<<"程序名字"<<argv[0]<<endl;
    // string arg1=argv[1];
    // if(arg1=="--help")
    //     cout<<"error"<<endl;
    
    rclcpp::init(argc,argv);
    auto node=make_shared<PersonNode>("person_node","zhangsan",18);//创建节点
    RCLCPP_INFO(node->get_logger(),"你好C++节点");
    node->eat("鱼香肉丝");
    rclcpp::spin(node);
    rclcpp::shutdown();
    
    return 0;
}