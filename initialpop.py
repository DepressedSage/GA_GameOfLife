import numpy as np

POPULATION=[]
POPSIZE=20
GENES=10

def init_pop():
    for i in range(POPSIZE):
        chromosome = np.random.choice([0,1], size=(GENES,GENES))
        POPULATION.append(chromosome)

def Flatten():
    for chromosome in POPULATION:
        chromosome = chromosome.flatten() #the LHS is important because chromosome.flatten() will just make a 1-d copy of the original 2-d chromosome, and not cause any changes in the original. So we need to assign it to the original to see the changes
        print("new chromosome\n")
        print(chromosome)
        print("\n")

init_pop()
Flatten()