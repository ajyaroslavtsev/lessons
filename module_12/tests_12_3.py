# -*- coding: utf-8 -*-

import unittest
from runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        tw = Runner('Pit')
        for _ in range(10):
            tw.walk()
        self.assertEqual(tw.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        tr = Runner('Den')
        for _ in range(10):
            tr.run()
        self.assertEqual(tr.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        tc_1 = Runner('Jon')
        tc_2 = Runner('Jack')
        for _ in range(10):
            tc_1.run()
            tc_2.walk()
        self.assertNotEqual(tc_1.distance, tc_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

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

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        tT = Tournament(90, self.usain, self.nik)
        result_tT = tT.start()
        self.assertTrue(result_tT.get(max(result_tT)) == 'Ник')
        self.all_results['tournament_1'] = result_tT

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        tT = Tournament(90, self.andrew, self.nik)
        result_tT = tT.start()
        self.assertTrue(result_tT.get(max(result_tT)) == 'Ник')
        self.all_results['tournament_2'] = result_tT

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        tT = Tournament(90, self.usain, self.andrew, self.nik)
        result_tT = tT.start()
        self.assertTrue(result_tT.get(max(result_tT)) == 'Ник')
        self.all_results['tournament_3'] = result_tT