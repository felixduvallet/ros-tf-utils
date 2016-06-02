cmake_minimum_required(VERSION 2.8.3)
project(calibration_tf_publisher)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rosparam
  tf
  tf2
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES calibration_tf_publisher
#  CATKIN_DEPENDS roscpp rosparam tf tf2
#  DEPENDS yaml
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)


add_executable(calibration_tf_publisher src/calibration_tf_publisher.cpp)
add_dependencies(calibration_tf_publisher ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(calibration_tf_publisher ${catkin_LIBRARIES})

#############
## Install ##
#############

install(TARGETS calibration_tf_publisher calibration_tf_publisher
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
