import random
import copy
import get_data

class Individual:
    def __init__(self, chromosome_length):
        self.chromosome = random.sample(range(1, chromosome_length +1), chromosome_length )
    def evaluate_fitness(self,data):
        data = [int(num) for num in data]
        A = [[data[i], data[i + 1]] for i in range(0, len(data) - 1)]
        n = len(data)
        fitness=0
        B = copy.deepcopy(A)
        # print("B=:",B)
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
            self.fitness=fitness
        return fitness
    def crossover(self, other):
        child = Individual(chromosome_length)
        child.chromosome = [0 for _ in range(chromosome_length)]

        new_chromosome = [item for pair in zip(self.chromosome, other.chromosome) for item in pair]
        print("new_chromosome:",new_chromosome)
        index = len(new_chromosome) - 1
        for i in range(len(self.chromosome)-1,-1,-1):
            while(new_chromosome[index] in child.chromosome):
                    index-=1
            child.chromosome[i]= int(new_chromosome[index])
        print("child chromosome: ",child.chromosome)

        return child
    def mutate(self):
        temp = self.chromosome[1]
        self.chromosome[1]=self.chromosome[0]
        self.chromosome[0]=temp
class Population:
    def __init__(self, size, chromosome_length):
        # print("init:",chromosome_length )
        self.individuals = [Individual(chromosome_length) for _ in range(size)]
        # print("indvs :")
        # for idv in self.individuals:
        #     print(idv.chromosome)
    def evaluate_population(self):
        for individual in self.individuals:
            individual.evaluate_fitness(data)
        return
    def selection(self):
        sorted_individuals = sorted(self.individuals, key=lambda x: x.evaluate_fitness(data), reverse=True)
        select_index=random.sample(range(0,len(self.individuals)//2), chromosome_length )
        return sorted_individuals[select_index[0]], sorted_individuals[select_index[1]]
    def evolve(self, mutation_rate):
        new_generation = []
        while len(new_generation) < len(self.individuals):
            parent1, parent2 = self.selection()
            child = parent1.crossover(parent2)
            child.mutate()
            new_generation.extend([child])
        self.individuals.extend(new_generation)
        self.individuals= sorted(self.individuals, key=lambda x: x.evaluate_fitness(data), reverse=True)
        self.individuals= self.individuals[:population_size]
        # for indv in self.individuals:
        #     print(indv.chromosome)


def solve(data,population_size,chromosome_length,mutation_rate,num_generations):
    print("data:", data)
    population = Population(population_size, chromosome_length)  # khởi tạo quẩn thể ban đầu
    print("Khoi tao quan the ban dau ")
    for indv in population.individuals:
        print(indv.chromosome)
    for generation in range(num_generations):
        print("generation ",generation+1)
        population.evaluate_population()
        print("Danh gia quan the da xong ")
        best_individual = max(population.individuals, key=lambda x: x.evaluate_fitness(data)) # chọn cá thể tốt nhất đàn
        print("chọn xong cá thể tốt nhất")
        print(f"Generation {generation + 1}: Best fitness = {best_individual.evaluate_fitness(data)}, Chromosome = {best_individual.chromosome}")
        population.evolve(mutation_rate)
        print("da chon xong quan the moi,quan the moi:")
        for indv in population.individuals:
            print(indv.chromosome)
    print("đã xong thuật toán thu đc kết quá :")
    best_individual = max(population.individuals, key=lambda x: x.evaluate_fitness(data))
    # print("population:",len(population.individuals))
    for indv in population.individuals:
        print("fitness:",indv.chromosome,indv.fitness)

    print(f"Final result: Best fitness = {best_individual.fitness}, Chromosome = {best_individual.chromosome}")
if __name__ == "__main__":
    data=get_data.get_data()
    population_size=10
    chromosome_length=len(data)-2
    mutation_rate=0.1
    num_generations=2

    solve(data, population_size, chromosome_length, mutation_rate, num_generations)
#to do: code lại hàm crossover
