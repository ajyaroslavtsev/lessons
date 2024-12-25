# -*- coding: utf-8 -*-

from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        tw = Runner('Pit')
        for _ in range(10):
            tw.walk()
        self.assertEqual(tw.distance, 50)

    def test_run(self):
        tr = Runner('Den')
        for _ in range(10):
            tr.run()
        self.assertEqual(tr.distance, 100)

    def test_challenge(self):
        tc_1 = Runner('Jon')
        tc_2 = Runner('Jack')
        for _ in range(10):
            tc_1.run()
            tc_2.walk()
        self.assertNotEqual(tc_1.distance, tc_2.distance)


if __name__ == '__main__':
    unittest.main()
  
