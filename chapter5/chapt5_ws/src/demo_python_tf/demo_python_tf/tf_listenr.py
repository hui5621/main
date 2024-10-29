import rclpy 
from rclpy.node import Node
import rclpy.time
from tf2_ros import TransformListener,Buffer #坐标发布器
from geometry_msgs.msg import TransformStamped#消息接口
from tf_transformations import euler_from_quaternion  #四元数函数转欧垃角
import math #角度转弧度函数

class TFBroadcaster(Node):
    
    def __init__(self):
        super().__init__("tf_broadcast")
        self.buffer_=Buffer()
        self.broadcast_=TransformListener(self.buffer_,self)
        self.timer_=self.create_timer(1.0,self.get_transform)#一秒钟发布100次tf
        # self.Publish_static_tf()
    def get_transform(self):
        """
            实时查询坐标关系  buffer_
        """
        try:
            result=self.buffer_.lookup_transform("base_link","bottle_link",
                                                 rclpy.time.Time(seconds=0.0),rclpy.time.Duration(seconds=1.0))
            #查询base_link到bottle_link之间的坐标关系，接受最新的消息，超时时间为1秒
            transform=result.transform
            self.get_logger().info(f"平移{transform.translation}")
            self.get_logger().info(f"旋转{transform.rotation}")
            rotation_euler=euler_from_quaternion([
                transform.rotation.x,
                transform.rotation.y,
                transform.rotation.z,
                transform.rotation.w
            ]
                
                )
            self.get_logger().info(f"旋转RPY{rotation_euler}")
        except Exception as e:
            self.get_logger().warn(f"获取坐标失败，原因{str(e)}")

def main():
  rclpy.init()
  node =TFBroadcaster()
  rclpy.spin(node)
  rclpy.shutdown()
  