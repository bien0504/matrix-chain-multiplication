import random
with open('input.txt', 'r') as file:
    data = file.read().split(',')
    data = [int(num) for num in data]
    n = len(data)
A = [[data[i], data[i+1]] for i in range(0, n-1)]
print("A:",A)
class Individual:
    def __init__(self, chromosome_length):
        self.chromosome = random.sample(range(1, chromosome_length +1), chromosome_length )
        self.fitness=self.evaluate_fitness()
    def get_fitness(self):
        return self.fitness
    def evaluate_fitness(self):
        fitness=0
        B=[]
        B=A.copy()
        contracted=[[0]*len(B) for _ in range(len(B))]
        for i in self.chromosome:
            fitness -= B[i - 1][0] * B[i - 1][1] * B[i][1]
            B[i - 1][1] = B[i][1]
            B[i][0] = B[i - 1][0]
            contracted[i-1][i]=1
            index=i
            while(index>0 and contracted[index-1][index]==1):
                index = index - 1
                B[index]=B[index+1]
            index=i
            while(index<len(B)-1 and contracted[index][index+1]==1):
                index = index + 1
                B[index]=B[index-1]
        print("fitness of",self.chromosome,"=",fitness)
        if(fitness==-392):
            print( self.chromosome)
        return fitness
    def crossover(self, other):
        child = Individual(chromosome_length)
        child.chromosome = [0 for _ in range(chromosome_length)]
        # print(child.chromosome)
        parent1_index = 0
        parent2_index = 0
        for i in range(len(self.chromosome)):
            if(i%2==0):
                while self.chromosome[parent1_index] in child.chromosome :
                     parent1_index+=1
                child.chromosome[i]=self.chromosome[parent1_index]
            else:
                while self.chromosome[parent2_index] in child.chromosome:
                     parent2_index+=1
                child.chromosome[i]=other.chromosome[parent2_index]

        return child
    def mutate(self):
        self.chromosome = self.chromosome[::-1]
class Population:
    def __init__(self, size, chromosome_length):
        # print("init:",chromosome_length )
        self.individuals = [Individual(chromosome_length) for _ in range(size)]
        for idv in self.individuals:
            print(idv.chromosome)
    # def evaluate_population(self):
        # for individual in self.individuals:
        #     individual.evaluate_fitness()
        # return
    def selection(self):
        sorted_individuals = sorted(self.individuals, key=lambda x: x.get_fitness(), reverse=True)
        return sorted_individuals[0], sorted_individuals[1]
    def evolve(self, mutation_rate):
        new_generation = []
        while len(new_generation) < len(self.individuals):
            parent1, parent2 = self.selection()
            child = parent1.crossover(parent2)
            child.mutate()
            new_generation.extend([child])
        self.individuals = new_generation
if __name__ == "__main__":

    population_size = 2
    chromosome_length = n-2
    mutation_rate = 0.0
    num_generations = 1
    population = Population(population_size, chromosome_length) # khởi tạo quẩn thể ban đầu
    for generation in range(num_generations):
        # population.evaluate_population()
        best_individual = max(population.individuals, key=lambda x: x.get_fitness()) # chọn cá thể tốt nhất đàn
        print(f"Generation {generation + 1}: Best fitness = {best_individual.get_fitness()}, Chromosome = {best_individual.chromosome}")
        population.evolve(mutation_rate)
    best_individual = max(population.individuals, key=lambda x: x.get_fitness())
    print("population:",len(population.individuals))
    for indv in population.individuals:
        print("fitness:",indv.chromosome,indv.fitness)

    print(f"Final result: Best fitness = {best_individual.fitness}, Chromosome = {best_individual.chromosome}")
    test=Individual(4)
    print(test.chromosome)
    print(test.fitness)
