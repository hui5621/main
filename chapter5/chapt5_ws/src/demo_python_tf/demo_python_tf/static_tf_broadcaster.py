import rclpy 
from rclpy.node import Node
from tf2_ros import StaticTransformBroadcaster #静态坐标发布器
from geometry_msgs.msg import TransformStamped #消息接口
from tf_transformations import quaternion_from_euler  #欧垃角转四元数函数
import math #角度转弧度函数

class StaticTFBroadcaster(Node):
    
    def __init__(self):
        super().__init__("static_tf_broadcast")
        self.static_broadcast_=StaticTransformBroadcaster(self)
        self.Publish_static_tf()
    def Publish_static_tf(self):
      """
        发布静态TF 从base_link到camera_link间的坐标关系（机械臂到相机）
      """
      transform=TransformStamped()
      transform.header.frame_id="base_link"#父坐标系
      transform.child_frame_id="camera_link"#子坐标系
      transform.header.stamp=self.get_clock().now().to_msg()#获取当前时间
      transform.transform.translation.x=0.5
      transform.transform.translation.y=0.3
      transform.transform.translation.z=0.6
      #欧拉角转四元数 q=x,y,z,w
      q=quaternion_from_euler(math.radians(180),0,0)#角度转弧度,rpy转换成四元组
      #旋转部分进行赋值
      transform.transform.rotation.x=q[0]
      transform.transform.rotation.y=q[1]
      transform.transform.rotation.z=q[2]
      transform.transform.rotation.w=q[3]
      #静态坐标关系发布出去
      self.static_broadcast_.sendTransform(transform)
      self.get_logger().info(f"发布静态TF：{transform}")

def main():
  rclpy.init()
  node =StaticTFBroadcaster()
  rclpy.spin(node)
  rclpy.shutdown()
  