cmake_minimum_required(VERSION 3.8)
project(demo_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)#添加依赖
find_package(rclcpp REQUIRED)#查找到对应的头文件和库文件
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
include_directories(include)#包含include头文件目录

add_executable(cpp_node src/cpp_node.cpp)#添加文件路径 cpp_node为可执行文件名字
add_executable(person_node src/person_node.cpp)#添加文件路径 cpp_node为可执行文件名字
add_executable(learn_auto  src/learn_auto.cpp)
add_executable(learn_shared_ptr  src/learn_shared_ptr.cpp)
add_executable(learn_lambda  src/learn_lambda.cpp)
add_executable(learn_funcational  src/learn_funcational.cpp)
add_executable(learn_thread  src/learn_thread.cpp)
# message(STATUS ${rclcpp_INCLUDE_DIRS})#头文件及其rclcpp依赖的头文件
# message(STATUS ${rclcpp_LIBRARIES})#库文件及rclcpp依赖的库文件
# target_include_directories(cpp_node PUBLIC ${rclcpp_INCLUDE_DIRS})#头文件包含
# target_link_libraries(cpp_node ${rclcpp_LIBRARIES})#库文件链接
ament_target_dependencies(cpp_node rclcpp)
ament_target_dependencies(person_node rclcpp)
# ament_target_dependencies(learn_auto rclcpp)

install(TARGETS cpp_node person_node learn_auto learn_shared_ptr learn_lambda learn_funcational learn_thread
  DESTINATION lib/${PROJECT_NAME}#把可执行文件cpp_node拷贝目的地lib文件下
)
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
