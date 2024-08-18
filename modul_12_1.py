#-*- coding: utf-8 -*-
import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runn = runner.Runner(name='Спортсмен № 1')
        for i in range(10):
            runn.walk()
        self.assertEqual(runn.distance,50)
    def test_run(self):
        runn = runner.Runner(name='Спортсмен № 2')
        for i in range(1, 11):
            runn.run()
        #self.assertEqual(runn.distance, 100)
        self.assertEqual(runn.distance, 90)
    def test_challenge(self):
        runner1 = runner.Runner(name='Спортсмен № 1')
        runner2 = runner.Runner(name='Спортсмен № 2')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance,runner2.distance)

if __name__ == '__main__':
    unittest.main()
