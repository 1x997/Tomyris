import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import cv2
from detectors import mobilenet_ssd


def get_path():
    return os.path.dirname(os.path.realpath(__file__)) + os.sep


class TestMobileNetSSDFunctionality(unittest.TestCase):

    def test_cars(self):
        frame = cv2.imread(get_path() + "cars1.png")
        mobilenet_ssd.initial_setup()
        objs = mobilenet_ssd.get_objects_of_interest(frame)
        print(objs)
        print("Len: " + str(len(objs)))
        for i in range(5):
            print("")
        self.assertGreater(len(objs), 4)

    def test_people(self):
        frame = cv2.imread(get_path() + "people1.png")
        mobilenet_ssd.initial_setup()
        objs = mobilenet_ssd.get_objects_of_interest(frame)
        print(objs)
        print("Len: " + str(len(objs)))
        for i in range(5):
            print("")
        self.assertGreater(len(objs), 1)

if __name__ == '__main__':
    unittest.main()
