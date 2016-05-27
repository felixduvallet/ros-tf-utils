
import unittest

from pose_to_tf.pose_to_tf_rebroadcaster import PoseToTFRebroadcaster


class TestCase(unittest.TestCase):
    def test_constructor(self):
        broad = PoseToTFRebroadcaster()
        self.assertIsNotNone(broad)


if __name__ == '__main__':
    unittest.main()
