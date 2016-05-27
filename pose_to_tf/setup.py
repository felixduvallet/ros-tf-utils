from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['pose_to_tf'],
    package_dir={'': 'src'},
    requires={'rospy'}
)

setup(**d)
