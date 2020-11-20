import genetic
import datetime

def get_fitness(genes, target):
    return sum(1 for ch_1, ch_2 in zip(genes, target) if ch_1 == ch_2)

def display(candidate, startTime):
    diffTime = datetime.datetime.now() - startTime
    print("{0}\t{1}\t{2}".format(candidate.Genes, candidate.Fitness, str(diffTime)))

def guess_password(target):
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    startTime = datetime.datetime.now()

    def fnGetFitness(genes):
        return get_fitness(genes, target)
    
    def fnDisplay(genes):
        return display(genes, startTime)
    
    optimalFitness = len(target)
    genetic.get_best(fnGetFitness, len(target), optimalFitness, geneset, fnDisplay)


if __name__ == "__main__":
    target = "a very looooooooooooooooooong sentenceeeeeeeeeeeeeeeeeee"
    guess_password(target)