
import unittest

from pose_to_tf.pose_to_tf_rebroadcaster import PoseToTFRebroadcaster
from geometry_msgs.msg import Pose


class TestCase(unittest.TestCase):
    def test_constructor(self):
        broad = PoseToTFRebroadcaster()
        self.assertIsNotNone(broad)

    def test_make_pose(self):
        p = PoseToTFRebroadcaster.make_stamped_pose([0, 1, 2])
        self.assertIsNotNone(p)
        self.assertEqual(0.0, p.position.x)
        self.assertEqual(1.0, p.position.y)
        self.assertEqual(2.0, p.position.z)

    def test_make_pose_empty(self):
        p = PoseToTFRebroadcaster.make_stamped_pose([])
        self.assertIsNone(p)

    def test_pose_to_tf(self):
        pose = Pose()
        pose.position.x = 1.0

        tf = PoseToTFRebroadcaster.pose_to_tf(pose, "child", "parent",
                                              time=1.0)

        self.assertIsNotNone(tf)
        self.assertEqual("child", tf.child_frame_id)
        self.assertEqual("parent", tf.header.frame_id)

        self.assertEqual(1.0, tf.transform.translation.x)


if __name__ == '__main__':
    unittest.main()
