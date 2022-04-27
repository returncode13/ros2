cmake_minimum_required(VERSION 3.5)
project(my_cpp_pkg)        #PROJECT_NAME is set to my_cpp_pkg



# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)

#for every new node add the following two lines

# add_executable  ==>  executable_name and file location under src    
# ament_target_dependencies ==> dependencies executable_name and its dependency (rclcpp)   
add_executable(cpp_node src/my_first_node.cpp)   
ament_target_dependencies(cpp_node rclcpp)


add_executable(robot_news_station src/robot_news_station.cpp)
ament_target_dependencies(robot_news_station rclcpp example_interfaces)


add_executable(smartphone src/smartphone.cpp)
ament_target_dependencies(smartphone rclcpp example_interfaces)
#the Executable is now compiled till this point 

#install the executable
install(TARGETS
  cpp_node                              #install executable to DESTINATION 
  robot_news_station
  smartphone
  DESTINATION lib/${PROJECT_NAME}       #DESTINATION set to install/lib/my_cpp_pkg
)

ament_package()
