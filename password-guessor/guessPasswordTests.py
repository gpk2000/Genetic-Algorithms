import datetime
import unittest
import genetic

def get_fitness(genes, target):
    return sum(1 for ch_1, ch_2 in zip(genes, target) if ch_1 == ch_2)

def display(candidate, startTime):
    diffTime = datetime.datetime.now() - startTime
    print("{0}\t{1}\t{2}".format(candidate.Genes, candidate.Fitness, str(diffTime)))

class GuessPasswordTests(unittest.TestCase):
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    startTime = datetime.datetime.now()

    def test_hello_world(self):
        target = "Hello World!"
        self.guess_password(target)

    def test_For_The_quick_brown_fox_jumps_over_the_lazy_dog(self):
        target = "The quick brown fox jumps over the lazy dog!."
        self.guess_password(target)

    def guess_password(self, target):
        startTime = datetime.datetime.now()

        def fnGetFitness(genes):
            return get_fitness(genes, target)
        
        def fnDisplay(genes):
            return display(genes, startTime)
        
        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness, self.geneset, fnDisplay)
        self.assertEqual(target, best.Genes)

if __name__ == "__main__":
    unittest.main()