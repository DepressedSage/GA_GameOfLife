import numpy as np
from numpy import random as r
ON = 1
OFF = 0
POPULATION=[]
POPSIZE=10000
GENES=10

def initialize_population(population=POPULATION,popsize=POPSIZE):
    for i in range(popsize):
        chromosome = np.random.choice([1,0], size=(GENES*GENES),p=[0.5,0.5])
        population.append(chromosome)
    return population

def reshape(population):
    for chromosome in population:
        chromosome = np.reshape(chromosome,(GENES,GENES))
    return population

def Flatten(population):
    for chromosome in population:
        chromosome = chromosome.flatten()
    return population

def neighbor_updation(arr):
    total = 0
    arr = np.reshape(arr,(GENES,GENES))
    new_arr = arr.copy()
    for i in range(GENES):
        for j in range(GENES):
            total = (arr[i, (j-1)%GENES] + arr[i, (j+1)%GENES] +
                     arr[(i-1)%GENES, j] + arr[(i+1)%GENES, j] +
                     arr[(i-1)%GENES, (j-1)%GENES] + arr[(i-1)%GENES, (j+1)%GENES] +
                     arr[(i+1)%GENES, (j-1)%GENES] + arr[(i+1)%GENES, (j+1)%GENES])
            if arr[i,j] == ON:
                if(total < 2) or (total > 3):
                    new_arr[i,j] = OFF
            else:
                if total == 3:
                    new_arr[i,j] = ON
    new_arr = new_arr.flatten()
    return new_arr

def check(t0,t1):
    for idx in range(len(t0)):
        if t0[idx] != t1[idx]:
            return True
    return False

def evaluate_one_entry(oscillator,period):
    temp = [oscillator]
    for idx in range(period):
        oscillator = neighbor_updation(oscillator)
        temp.append(oscillator)
    for i in range(period):
        if np.array_equal(temp[i],temp[i+1]) is True:
            return False
    if np.array_equal(temp[0],temp[period-1]) is True:
        return True

def evaluate_population(population,period):
    selected_parents = []
    for itr in population:
        if evaluate_one_entry(itr,period):
            selected_parents.append(itr)
    return selected_parents

def crossover(parent1, parent2, crossover_rate=0.5):
    offspring = []
    for i in range(len(parent1)):
        if np.random.random() < crossover_rate:
            offspring.append(parent1[i])
        else:
            offspring.append(parent2[i])
    return offspring

def crossover_population(population,crossover_rate=0.5):
    offspring_pop = list()
    for i in range(len(population)):
        tmp_pop = population
        parent1 = population[i]
        idx = np.random.choice(range(len(tmp_pop)))
        parent2 = tmp_pop[idx]
        offspring1 = crossover(parent1, parent2,crossover_rate)
        offspring_pop.append(offspring1)
        offspring2 = [1-i for i in offspring1]
        offspring_pop.append(offspring2)
    return offspring_pop

def mutation(offspring_population, mutation_rate=0.5):
    mutated_offspring = offspring_population.copy()
    for offspring in mutated_offspring:
        for gene in range(len(offspring)):
            if np.random.random() < mutation_rate:
                new_gene = np.random.choice([ON,OFF],p=[0.5,0.5])
                offspring[gene] = new_gene
    return mutated_offspring

def genetic_algorithm(period=2,crossover_rate=0.2,mutation_rate=0.6,generations=2):
    population = initialize_population()
    selected_parents = population
    for i in range(generations):
        selected_parents = evaluate_population(population,period)
        if len(selected_parents) < 10:
           return selected_parents
        print(len(selected_parents))
        offspring_population = crossover_population(selected_parents,crossover_rate)
        print(len(offspring_population))
        mutated_offspring = mutation(offspring_population,mutation_rate)
        print(len(mutated_offspring))
        population = mutated_offspring
        print(f"Epoch {i} complete")
    return selected_parents

population = genetic_algorithm(generations=10)
for i in population:
    print(i.tolist())


