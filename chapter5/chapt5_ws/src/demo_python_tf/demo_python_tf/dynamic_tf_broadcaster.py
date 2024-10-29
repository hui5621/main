import rclpy 
from rclpy.node import Node
from tf2_ros import TransformBroadcaster #坐标发布器
from geometry_msgs.msg import TransformStamped #消息接口
from tf_transformations import quaternion_from_euler  #欧垃角转四元数函数
import math #角度转弧度函数

class TFBroadcaster(Node):
    
    def __init__(self):
        super().__init__("tf_broadcast")
        self.broadcast_=TransformBroadcaster(self)
        self.timer_=self.create_timer(0.01,self.Publish__tf)#一秒钟发布100次tf
        # self.Publish_static_tf()
    def Publish__tf(self):
      """
        发布静态TF 从camera_link到bottle_link间的坐标关系（相机到瓶子）
      """
      transform=TransformStamped()
      transform.header.frame_id="camera_link"#父坐标系
      transform.child_frame_id="bottle_link"#子坐标系
      transform.header.stamp=self.get_clock().now().to_msg()#获取当前时间
      transform.transform.translation.x=0.2
      transform.transform.translation.y=0.3
      transform.transform.translation.z=0.5
      #欧拉角转四元数 q=x,y,z,w
      q=quaternion_from_euler(0,0,0)#角度转弧度,rpy转换成四元组
      #旋转部分进行赋值
      transform.transform.rotation.x=q[0]
      transform.transform.rotation.y=q[1]
      transform.transform.rotation.z=q[2]
      transform.transform.rotation.w=q[3]
      #静态坐标关系发布出去
      self.broadcast_.sendTransform(transform)
      self.get_logger().info(f"发布TF：{transform}")

def main():
  rclpy.init()
  node =TFBroadcaster()
  rclpy.spin(node)
  rclpy.shutdown()
  