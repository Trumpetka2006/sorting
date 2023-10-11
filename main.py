from sorting.Bublinka import *
import sorting.crapsort as crapsort
import time

seznam = []

seznam = get_random_list(10 , max= 5)

#print(remove_even_zeros(seznam))

startTime = time.process_time()

print(buble_sort(seznam))

endTime = time.process_time()
finalTime = endTime - startTime
finalTime *= 1000
print(f"Bublinka: {round(finalTime,5)} ms")

startTime = time.process_time()

print(crapsort.sort(seznam))

endTime = time.process_time()
finalTime = endTime - startTime
finalTime *= 1000
print(f"CrapSort: {round(finalTime,5)} ms")

startTime = time.process_time()

seznam.sort
print(seznam)

endTime = time.process_time()
finalTime = endTime - startTime
finalTime *= 1000
print(f"PySort: {round(finalTime,5)} ms")

