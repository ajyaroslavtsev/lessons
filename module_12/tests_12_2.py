# -*- coding: utf-8 -*-

import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrew = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            result = {place: runner.name for place, runner in value.items()}
            print(result)

    def test_tournament_1(self):
        tT = Tournament(90, self.usain, self.nik)
        result_tT = tT.start()
        self.assertTrue(result_tT.get(max(result_tT)) == 'Ник')
        self.all_results['tournament_1'] = result_tT

    def test_tournament_2(self):
        tT = Tournament(90, self.andrew, self.nik)
        result_tT = tT.start()
        self.assertTrue(result_tT.get(max(result_tT)) == 'Ник')
        self.all_results['tournament_2'] = result_tT

    def test_tournament_3(self):
        tT = Tournament(90, self.usain, self.andrew, self.nik)
        result_tT = tT.start()
        self.assertTrue(result_tT.get(max(result_tT)) == 'Ник')
        self.all_results['tournament_3'] = result_tT


if __name__ == '__main__':
    unittest.main()