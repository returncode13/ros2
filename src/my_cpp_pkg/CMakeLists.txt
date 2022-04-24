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

#executable_name and file location under src
add_executable(cpp_node src/my_first_node.cpp)   
#dependencies executable_name and its dependency (rclcpp)
ament_target_dependencies(cpp_node rclcpp)
#the Executable is now compiled till this point 

#install the executable
install(TARGETS
  cpp_node                              #install executable to DESTINATION 
  DESTINATION lib/${PROJECT_NAME}       #DESTINATION set to install/lib/my_cpp_pkg
)

ament_package()
