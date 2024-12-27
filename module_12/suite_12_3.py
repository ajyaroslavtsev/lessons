# -*- coding: utf-8 -*-

import unittest
from tests_12_3 import RunnerTest, TournamentTest


rt_ST = unittest.TestSuite()
rt_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
rt_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(rt_ST)

