
import rclpy
from rclpy.node import Node
import requests
from example_interfaces.msg import String#消息接口
from queue import Queue

class NovelPubNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.get_logger().info(f"{node_name},启动！")
        self.novels_queue_ = Queue() # 创建队列，存放小说
        self.novel_publisher_=self.create_publisher(String,"novel",10)#创建话题的发布者
        self.create_timer(5,self.time_callback)#间隔5秒发布
        
    def time_callback(self):
        # self.novel_publisher_.publish() 发布
        if self.novels_queue_.qsize() > 0: # 队列中有数据，取出发布一行
            line=self.novels_queue_.get()
            msg=String()#组装成消息
            msg.data=line
            self.novel_publisher_.publish(msg)
            self.get_logger().info(f"{msg}：发布了")
    def download(self,url):
        response=requests.get(url)
        response.encoding='utf-8'
        text=response.text
        self.get_logger().info(f"{url},{len(text)}")
        for line in response.text.splitlines(): # 按行分割，放入队列
            self.novels_queue_.put(line)
       

def main():
    rclpy.init()
    node = NovelPubNode('novel_pub')
    node.download('http://0.0.0.0:8000/novel1.txt')

    rclpy.spin(node)
    rclpy.shutdown()
