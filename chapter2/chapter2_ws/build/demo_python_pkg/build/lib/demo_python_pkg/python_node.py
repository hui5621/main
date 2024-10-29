import rclpy
from rclpy.node import Node

def main():
    rclpy.init()#初始化工作、分配资源
    node=Node("python_node")#创建节点，声明node实例
    node.get_logger().info("你好 python节点")#打印日志
    node.get_logger().warn("你好 python节点")#打印日志
    rclpy.spin(node)#运行节点
    rclpy.shutdown()#清理资源
    
    
    
    
    
#export RCUTILS_CONSOLE_OUTPUT_FORMAT=[{function_name}:{line_number}]:{message} 终端环境变量配置：  方法名：行号：内容
#export PYTHONPATH=/home/wang/桌面/item/chapter2/install/demo_python_pkg/lib/python3.10/site-packages:$PYTHONPATH 环境变量修改

#printenv | grep PYTHON 查看PATHONPATH信息
#ros2 pkg create demo_python_pkg --build-type ament_python --license Apache-2.0 创建功能包
#colon build 构建功能包（build：中间文件、install：构建结果的文件夹、log） 以当前目录为基准，构建当前及其子目录下的功能包；

#source install/setup.bash      修改环境变量
#ros2 run  demo_python_pkg python_node

