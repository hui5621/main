import launch
# import launch.launch_description_sources
import launch_ros.parameter_descriptions
from ament_index_python.packages import get_package_share_directory
import os

import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    # 获取默认路径
    robot_name_in_model = "fishbot"
    urdf_tutorial_path = get_package_share_directory('fishbot_description')
    default_model_path = urdf_tutorial_path + '/urdf/fishbot/fishbot.urdf.xacro'
    default_world_path = urdf_tutorial_path + '/world/custom_room.world'
    # 为 Launch 声明参数
    action_declare_arg_mode_path = launch.actions.DeclareLaunchArgument(
        name='model', default_value=str(default_model_path),
        description='URDF 的绝对路径')
    # 获取文件内容生成新的参数
    robot_description = launch_ros.parameter_descriptions.ParameterValue(
        launch.substitutions.Command(
            ['xacro ', launch.substitutions.LaunchConfiguration('model')]),
        value_type=str)
  	
    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}]
    )
    # 通过 IncludeLaunchDescription 包含另外一个 launch 文件
    launch_gazebo = launch.actions.IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory(
            'ros_gz_sim'), '/launch', '/gz_sim.launch.py']),
      	# 传递参数
        launch_arguments=[('world', default_world_path),('verbose','true')]
    )
    # 请求 Gazebo 加载机器人
    spawn_entity_node = launch_ros.actions.Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-topic', '/robot_description',
                   '-entity', robot_name_in_model, ])
    
    # 加载并激活 fishbot_joint_state_broadcaster 控制器
    load_joint_state_controller = launch.actions.ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active',
            'fishbot_joint_state_broadcaster'],
        output='screen'
    )
    
    # 加载并激活 fishbot_effort_controller 控制器
    load_fishbot_effort_controller = launch.actions.ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active','fishbot_effort_controller'], 
        output='screen')
    
    load_fishbot_diff_drive_controller = launch.actions.ExecuteProcess(
        cmd=['ros2', 'control', 'load_controller', '--set-state', 'active','fishbot_diff_drive_controller'], 
        output='screen')
    return launch.LaunchDescription([
        action_declare_arg_mode_path,
        robot_state_publisher_node,
        launch_gazebo,
        spawn_entity_node,
        # 事件动作，当加载机器人结束后执行    
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=spawn_entity_node,
                on_exit=[load_joint_state_controller],)
            ),
        # 事件动作，load_fishbot_effort_controller
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=spawn_entity_node,
                on_exit=[load_fishbot_effort_controller],)
            ),
        # # 事件动作，load_fishbot_diff_drive_controller
        # launch.actions.RegisterEventHandler(
        # event_handler=launch.event_handlers.OnProcessExit(
        #     target_action=load_joint_state_controller,
        #     on_exit=[load_fishbot_diff_drive_controller],)
        #     ),
      
    ])


# def generate_launch_description():
#     # 获取功能包的share路径
#     urdf_package_path=get_package_share_directory("fishbot_description")
#     default_xacro_path=os.path.join(urdf_package_path,"urdf","fishbot/fishbot.urdf.xacro")
#     default_gazebo_world_path =os.path.join(urdf_package_path,"world","custom_room.world")
#     #声明一个urdf目录的参数，方便修改
#     action_declare_arg_mode_path=launch.actions.DeclareLaunchArgument(
#         name="model",default_value=str(default_xacro_path),description="加载的模型文件路经"
#     )
#     # 通过文件路径获取文件内容，并转换成参数值对象，以供传入robot_state_publisher
#     substitutions_command_result=launch.substitutions.Command(["xacro ",launch.substitutions.LaunchConfiguration("model")])#执行xacro命令，查看内容和
#     robot_description_value=launch_ros.parameter_descriptions.ParameterValue(substitutions_command_result,value_type=str)#转换成参数值对象
#     action_robot_state_publisher=launch_ros.actions.Node(
#         package="robot_state_publisher",
#         executable="robot_state_publisher",
#         parameters=[{"robot_description":robot_description_value}]#调用
#     )
#     # action_joint_state_publisher=launch_ros.actions.Node(
#     #     package="joint_state_publisher",
#     #     executable="joint_state_publisher",
#     # )
#     # action_rviz_node=launch_ros.actions.Node(
#     #     package="rviz2",
#     #     executable="rviz2",
#     # )

#     #启动gazebo节点
#     # ros2 launch gazebo_ros gazebo.launch.py world:=***.world
#     action_launch_gazebo=launch.actions.IncludeLaunchDescription(
#         launch.launch_description_sources.PythonLaunchDescriptionSource(
#             [get_package_share_directory("gazebo_ros"),"/launch","/gazebo.launch.py"]
#         ),
#         launch_arguments=[("world",default_gazebo_world_path),("verbose","true")]
#     )
#     # # 关节状态发布节点
#     # joint_state_publisher_node = launch_ros.actions.Node(
#     #     package='joint_state_publisher',
#     #     executable='joint_state_publisher',
#     # )

#     # # RViz 节点
#     # rviz_node = launch_ros.actions.Node(
#     #     package='rviz2',
#     #     executable='rviz2',
#     #     arguments=['-d', default_rviz_config_path]
#     # )
#     return launch.LaunchDescription([
#         action_declare_arg_mode_path,
#         # joint_state_publisher_node,
#         action_robot_state_publisher,
#         action_launch_gazebo,
#         # rviz_node
#     ])