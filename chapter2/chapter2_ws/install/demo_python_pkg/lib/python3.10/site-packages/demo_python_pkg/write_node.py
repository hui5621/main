import rclpy
from rclpy.node import Node
from demo_python_pkg.person_node import PersonNode
class WriteNode(PersonNode):
    def __init__(self,node_name:str,name:str,age:int,book:str)->None:
        print("Write被调用了")
        super().__init__(node_name,name,age)#调用父类的__init__方法
        self.book=book

def main():
    rclpy.init()
    node=WriteNode("write_zhangsan","章三",28,"ROS机器学习")
    node.eat("饭")
    rclpy.spin(node)
    rclpy.shutdown()