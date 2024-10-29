import launch
import launch_ros

def generate_launch_description():
    #产生launch描述
    #1、声明一个launch的参数
    #2、在把launch的参数手动传递给某个结点
    action_declare_arg_max_spped = launch.actions.DeclareLaunchArgument('launch_max_speed', default_value='2.0')

    action_node_turtle_control = launch_ros.actions.Node(
        package='demo_cpp_service',
        executable="turtle_control",
        output='screen',#输出到屏幕
        parameters=[{'max_speed': launch.substitutions.LaunchConfiguration(
  'launch_max_speed', default='2.0')}],

    )
    action_node_patrol_client = launch_ros.actions.Node(
        package='demo_cpp_service',#功能包名字
        executable="patrol_client",#可执行文件
        output='log',#日志
    )
    action_node_turtlesim_node = launch_ros.actions.Node(
        package='turtlesim',
        executable='turtlesim_node',
        output='both',#都可以
    )
   # 合成启动描述并返回
    launch_description = launch.LaunchDescription([
        action_declare_arg_max_spped,
        action_node_turtle_control,
        action_node_patrol_client,
        action_node_turtlesim_node
    ])
    return launch_description
