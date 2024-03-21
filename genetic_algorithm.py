import random

with open('data.txt', 'r') as file:
    data = file.read().split(',')
    data = [int(num) for num in data]
    n = len(data)

A = [[data[i], data[i+1]] for i in range(0, n-1)]
print("A:",A)

class Individual:
    def __init__(self, chromosome_length):
        self.chromosome = random.sample(range(1, chromosome_length - 1), chromosome_length - 2)
        self.fitness = 0
        self.chain=A
    def evaluate_fitness(self):
        fitness=0
        B=A.copy()
        contracted=[[0]*len(B) for _ in range(len(B))]
        print("i:",self.chromosome)
        for i in self.chromosome:
            fitness -= B[i - 1][0] * B[i - 1][1] * B[i][1]
            B[i - 1][1] = B[i][1]
            B[i][0] = B[i - 1][0]
            contracted[i-1][i]=1
            index=i
            print("index=",index)
            while(index>0 and contracted[index-1][index]==1 and contracted[index-2][index-1]==1):
                index = index - 1
                B[index]=B[index+1]
            # else:
            #     break
            index=i
            while(index<len(B)-1 and contracted[index-1][index]==1 and contracted[index][index+1]==1):
                index = index + 1
                B[index]=B[index-1]
            # else:
            #     break

            print("B after ", i, ":", B, fitness)
            # print("contracted:",contracted)
        self.fitness = fitness

    def crossover(self, other):
        crossover_point = random.randint(0, len(self.chromosome) - 1)
        child1_chromosome = self.chromosome[:crossover_point] + other.chromosome[crossover_point:]
        child2_chromosome = other.chromosome[:crossover_point] + self.chromosome[crossover_point:]
        child1=Individual(len(self.chromosome))
        child2=Individual(len(self.chromosome))
        child1.chromosome=child1_chromosome
        child2.chromosome=child2_chromosome
        return child1,child2

    def mutate(self, mutation_rate):
        for i in range(len(self.chromosome)):
            if random.random() < mutation_rate:
                self.chromosome[i] = 1 if self.chromosome[i] == 0 else 0
    def chain(self):
        B=[]


class Population:
    def __init__(self, size, chromosome_length):
        self.individuals = [Individual(chromosome_length) for _ in range(size)]

    def evaluate_population(self):
        for individual in self.individuals:
            individual.evaluate_fitness()

    def selection(self):
        sorted_individuals = sorted(self.individuals, key=lambda x: x.fitness, reverse=True)
        return sorted_individuals[0], sorted_individuals[1]

    def evolve(self, mutation_rate):
        new_generation = []
        while len(new_generation) < len(self.individuals):
            parent1, parent2 = self.selection()
            child1, child2 = parent1.crossover(parent2)
            child1.mutate(mutation_rate)
            child2.mutate(mutation_rate)
            new_generation.extend([child1, child2])
        self.individuals = new_generation

if __name__ == "__main__":
    population_size = 2
    chromosome_length = n
    mutation_rate = 0.1
    num_generations = 1

    population = Population(population_size, chromosome_length)

    for generation in range(num_generations):
        population.evaluate_population()
        best_individual = max(population.individuals, key=lambda x: x.fitness)
        print(
            f"Generation {generation + 1}: Best fitness = {best_individual.fitness}, Chromosome = {best_individual.chromosome}")
        population.evolve(mutation_rate)

    best_individual = max(population.individuals, key=lambda x: x.fitness)
    print(f"Final result: Best fitness = {best_individual.fitness}, Chromosome = {best_individual.chromosome}")