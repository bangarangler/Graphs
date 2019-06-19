import random

[0,1,2,3,4]

for i in range(0,3):
    i = 3
    random_index = random.randint(0,4)

def fisher_yates_shuffle(l):
    for i in range(0, len(l)):
        random_index = random.randint(0, len(l) - 1)
        l[random_index], l[i] = l[i], l[random_index]
