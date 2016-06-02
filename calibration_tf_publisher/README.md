# Calibration TF publisher

Store your calibration TF as a yaml file and have this node publish it as a
static TF by loading it from the parameter server.

This is exactly the static_transform_publisher that exists in the ROS
[geometry2](https://github.com/ros/geometry2) package, with [my
modifications](https://github.com/ros/geometry2/pull/179).


Usage:

    # Load the calibration TF into the param server.
    rosparam load launch/example_calibration.yaml /calibration_transform
    # Start the TF publisher with this parameter name.
    rosrun calibration_tf_publisher calibration_tf_publisher /calibration_transform

Alternatively:

    roslaunch calibration_tf_publisher calibration_tf_publisher.launch calibration_file:=launch/example_calibration.yaml

The data in the calibration parameter must be a valid TF, with a child frame,
parent frame, and transform (translation and rotation).
