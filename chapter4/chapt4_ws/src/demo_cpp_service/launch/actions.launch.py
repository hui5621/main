# import cmd
import launch
import launch.launch_description_sources
import launch_ros
from ament_index_python.packages import get_package_share_directory
#通过工程包名字获取get_package_share_directory目录
def generate_launch_description():
    action_declare_startup_rqt = launch.actions.DeclareLaunchArgument('startup_rqt', default_value='False')
    startup_rqt=launch.substitutions.LaunchConfiguration('startup_rqt', default='False')

    #1、动作1-启动其他launch
    multisim_launch_path=[get_package_share_directory("turtlesim"),"/launch","/multisim.launch.py"]
    action_include_launch =launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(
            # multisim_launch_path
            [get_package_share_directory("turtlesim"),"/launch","/multisim.launch.py"]
        )
    )
    #2、动作2-打印数据
    action_log_info=launch.actions.LogInfo(msg=str(multisim_launch_path))
     #3、动作3-执行进程，执行一个命令行 ros2 topic list
    action_topic_list=launch.actions.ExecuteProcess(
        # cmd=["ros2","topic","list"],output="screen"
        condition=launch.conditions.IfCondition(startup_rqt),
        cmd=["rqt"]
    )
     #4、动作4-组织动作成组，把多个动作放到一起
    action_group=launch.actions.GroupAction(
        # #动作5-定时器
        actions=[
        launch.actions.TimerAction(
            period=2.0, actions=[action_include_launch]
        ),  # 启动2个小海龟模拟器
        launch.actions.TimerAction(
            period=4.0, actions=[action_topic_list]
        ),  # 执行一个命令行 ros2 topic list
    ]
    )
    # return launch.launch_description([
    #     action_log_info,
    #     action_group
    # ])
# 合成启动描述并返回
    launch_description = launch.LaunchDescription([
        action_log_info,
        action_group,
        action_declare_startup_rqt,
    ])
    return launch_description
