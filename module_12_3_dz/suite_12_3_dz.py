import unittest
import run_test_12_3_dz
import tour_test_12_3_dz

runTs = unittest.TestSuite()
runTs.addTest(unittest.TestLoader().loadTestsFromTestCase(tour_test_12_3_dz.TournamentTest))
runTs.addTest(unittest.TestLoader().loadTestsFromTestCase(run_test_12_3_dz.RunnerTest))

test_run = unittest.TextTestRunner(verbosity=2)
test_run.run(runTs)
