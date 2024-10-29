import rclpy
from rclpy.node import Node

class PersonNode(Node):
    def __init__(self,node_name:str,name:str,age:int)->None:
        super().__init__(node_name)
        self.name=name
        self.age=age
        pass
    def eat(self,food_name:str):
        """
        方法：吃东西
        :food_name：名字
        """
        # print(f"{self.name},{self.age}爱吃{food_name}")
        self.get_logger().info(f"{self.name},{self.age}爱吃{food_name}")#改为ros2节点

def main():
    rclpy.init()
    node=PersonNode("zhangsan","张三",18)
    node.eat("饭")
    rclpy.spin(node)
    rclpy.shutdown()