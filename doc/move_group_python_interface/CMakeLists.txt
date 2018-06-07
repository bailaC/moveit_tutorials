cmake_minimum_required(VERSION 2.8.3)
project(move_group_python_interface)

find_package(catkin REQUIRED)

catkin_python_setup()

catkin_package()

catkin_install_python(PROGRAMS scripts/move_group_python_interface_tutorial
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
