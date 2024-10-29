#include "rclcpp/rclcpp.hpp"  //c++的头文件
using namespace std;
int main(int argc,char ** argv)//程序入口参数
{
    // cout<<"参数变量"<<argc<<endl;
    // cout<<"程序名字"<<argv[0]<<endl;
    // string arg1=argv[1];
    // if(arg1=="--help")
    //     cout<<"error"<<endl;
    
    rclcpp::init(argc,argv);
    auto node=make_shared<rclcpp::Node>("cpp_node");//创建节点
    RCLCPP_INFO(node->get_logger(),"你好C++节点");
    rclcpp::spin(node);
    rclcpp::shutdown();
    
    return 0;
}
