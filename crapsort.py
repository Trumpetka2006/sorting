import time
import random

def sort(data):
    start = time.process_time()
    unsorted = True
    attemps = 0
    while unsorted:
        for index in range(len(data) - 1):
            if not data[index] <= data[index + 1]:
                attemps += 1
                random.shuffle(data)
                break
            elif index == len(data) - 2:
                unsorted = False
    endtime = time.process_time()

    """ print(data)
    totaltime = endtime - start
    totaltime = totaltime * 1000
    totaltime = round(totaltime,5)
    print(f"Done in: {totaltime} ms!") """
    print(f"It only take {attemps} attemps. ;)")

    return(data)

#somenumbers = [0,1,2,3,5,4,]
#sort(somenumbers)s
input ()
