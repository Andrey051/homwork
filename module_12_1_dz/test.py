import unittest
import runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walks = runner.Runner("Жора")
        for i in range(10):
            walks.walk()
        self.assertEqual(walks.distance,50)

    def test_run(self):
        runs = runner.Runner("Вася")
        for i in range(10):
            runs.run()
        self.assertEqual(runs.distance,100)

    def test_chalendg(self):
        wal = runner.Runner("Федя")
        runa = runner.Runner("Леша")
        for i in range(10):
            wal.walk()
            runa.run()
        self.assertNotEqual(wal.distance,runa.distance)


