# Calibration TF publisher

This is essentially the static_transform_publisher with one additional feature:
you can pass a ROS parameter that contains a calibration TF.

Usage:

    rosrun calibration_tf_publisher calibration_tf_publisher /calibration_transform

The data in the `/calibration_transform` parameter must be a valid TF, e.g.:

     $ rosparam get /calibration_transform/
     child_frame_id: robot_calibration
     header:
       frame_id: world
     transform:
       rotation: {w: 0.38720459109, x: -0.62908825919, y: 0.210952809338, z: 0.640171445021}
       translation: {x: 0.76, y: 0.5, z: 1.0}

This yaml can also contain a `period: NN` element, indicating the publishing
period in milliseconds (otherwise the default is 10 msecs).