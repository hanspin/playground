from Roadlight import *
import unittest


class RoadlightTestcase(unittest.TestCase):

    def setUp(self):
        self.rl = Roadlight()
        self.rl.recharge()

    def test_switch_on(self):
        self.rl.switch_on()
        self.assertEqual(self.rl.battery, 0)

    def test_switch_off(self):
        # TODO: implement this
        raise NotImplementedError

    def test_recharge(self):
        # TODO: implement this
        pass
