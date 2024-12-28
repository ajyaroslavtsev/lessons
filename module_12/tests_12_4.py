# -*- coding: utf-8 -*-

import unittest
import logging

from rt_with_exceptions import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            tw = Runner('Pit', speed=-5)
            for _ in range(10):
                tw.walk()
            self.assertEqual(tw.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            tr = Runner(name=25)
            for _ in range(10):
                tr.run()
            self.assertEqual(tr.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        tc_1 = Runner('Jon')
        tc_2 = Runner('Jack')
        for _ in range(10):
            tc_1.run()
            tc_2.walk()
        self.assertNotEqual(tc_1.distance, tc_2.distance)


if __name__ == '__main__':
    root_logger= logging.getLogger()
    root_logger.setLevel(logging.INFO)
    handler = logging.FileHandler('runner_tests.log', 'w', 'utf-8')
    formatter = logging.Formatter('%(levelname)s | %(message)s')
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)

    unittest.main()