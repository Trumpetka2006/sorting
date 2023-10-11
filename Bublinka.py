import random
from copy import deepcopy

def get_random_list(n, min = 0, max = 100):
    seznam = []
    if min >= max:
        raise ValueError("min must be smaller then max")
    for i in range(n):
        seznam.append(random.randint(min,max))
    return seznam

def remove_even_zeros(list_):
    even = False
    output = []
    for num in list_:
        if num == 0:
            if not even: output.append(num)
            if even: even = False 
            else: even =True
        else: 
            output.append(num)
    return output
                
def buble_sort(list_):
    process = deepcopy(list_)
    for lengh in range(len(list_)):
        
        for index in range(len(list_) - 1):
            if process[index] > process[index + 1]:
                process[index], process[index + 1]  = process[index + 1], process[index]
                #process[index + 1] = list_[index]
            #list_ = deepcopy(process)
    return process


    
