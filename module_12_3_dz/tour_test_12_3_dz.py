import unittest
import runner as rn


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.runner_1 = rn.Runner('Усэйн', 10)
        self.runner_2 = rn.Runner("Андрей", 9)
        self.runner_3 = rn.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"Тест: {key}")
            for key, value in value.items():
                print(f'{key}: {value.name}')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_1(self):
        test_tourn_1 = rn.Tournament(90, self.runner_1, self.runner_3)
        result = test_tourn_1.start()
        self.assertTrue(result[2], self.runner_3)
        self.all_results['test_tourn_1'] = result

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_2(self):
        test_tourn_2 = rn.Tournament(90, self.runner_2, self.runner_3)
        result = test_tourn_2.start()
        self.assertTrue(result[2], self.runner_3)
        self.all_results['test_tourn_2'] = result

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tournament_3(self):
        test_tourn_3 = rn.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = test_tourn_3.start()
        self.assertTrue(result[3], self.runner_3)
        self.all_results['test_tourn_3'] = result


if __name__ == "__main__":
    unittest.main()
