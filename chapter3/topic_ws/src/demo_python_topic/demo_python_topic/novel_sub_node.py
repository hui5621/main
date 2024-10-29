import espeakng
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from queue import Queue
import threading
from queue import Queue
import time

class NovelSubNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.get_logger().info(f"{node_name},启动！")
        self.novel_queue_=Queue()
        self.novel_subscriber=self.create_subscription(String,"novel",self.novel_callback,10)
        self.speech_thread_ = threading.Thread(target=self.speak_thread)
        self.speech_thread_.start()
    def novel_callback(self,msg):
        self.novel_queue_.put(msg.data)
    def speak_thread(self):
            speaker = espeakng.Speaker()
            speaker.voice = 'zh'
            while rclpy.ok():#检测当前ROS上下文是否Ok
                if self.novel_queue_.qsize() > 0:
                    text = self.novel_queue_.get()
                    self.get_logger().info(f'正在朗读 {text}')
                    speaker.say(text)
                    speaker.wait()
                else:
                    time.sleep(1)
def main():
    rclpy.init()
    node = NovelSubNode('novel_read')
    rclpy.spin(node)
    rclpy.shutdown()