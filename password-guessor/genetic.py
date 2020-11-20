import random

class Chromosome:
    Genes = []
    Fitness = []

    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness


def _generate_parent(length, geneSet, get_fitness):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    genes = ''.join(genes)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)


def _mutate(parent, geneSet, get_fitness):
    index = random.randrange(0, len(parent.Genes))
    childGenes = list(parent.Genes)
    newGene, alternative = random.sample(geneSet, 2)
    childGenes[index] = newGene if childGenes[index] != newGene \
                                else alternative
    genes = ''.join(childGenes)
    fitness = get_fitness(childGenes)
    return Chromosome(genes, fitness)


def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
    random.seed()
    bestParent = _generate_parent(targetLen, geneSet, get_fitness)
    display(bestParent)
    if bestParent.Fitness >= optimalFitness:
        return bestParent
    
    while True:
        child = _mutate(bestParent, geneSet, get_fitness)
        if child.Fitness <= bestParent.Fitness:
            continue
        display(child)
        if child.Fitness >= optimalFitness:
            return child
        bestParent = child