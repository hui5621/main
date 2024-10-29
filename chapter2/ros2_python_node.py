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

if __name__ == "__main__":
    main()