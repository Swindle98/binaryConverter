import random
import time
import threading
import sys

from queue import Queue

def RandomNum(): # a function that generates a random number at a random time.
  time.sleep(random.random())
  randnum = random.randint(1, 100000000)  
  #print(randnum)

  return randnum

def randQ(i): # takes the random number and adds it to the queue
    while i :
        q.put(RandomNum())
        i -= 1

def sam_counter(number):
    import math

    number = int(number)
    #print('start number =', number)
    onumber = number
    if number == 0:
        print(0)
    else:

        #use the log of the number to find out how many bits are required to express the number in binary.
        log = int(math.log2(number)) + 1
        columns = list(range(log))
        #print('There will be ', len(columns), ' bits', int(len(columns) / 8) + 1, 'bytes') #reports the number of bits
        #print(log)
        #find the decimal value of each bit (the columns of the grid)
        colval = []
        for value in columns:
            colval.append(2 ** value)
            #print('\n colval value =', colval)


        #starting from the left most bit if the value of the bit can be subtracted from the starting number, if it can it is the bit is tossed and the number is reduced, if it cant a zero is added to the bit.
        bindict ={} #a dictionary holding both the column values and the binary values.
        while len(colval):
            if colval[-1] <= number: #making the bit into a 1
                bindict[colval[-1]]= '1'
                number -= colval.pop()
                #print('  number=',number)


            else:
                bindict[colval.pop()]= '0' #making the bit a 0
                #print('  \nnumber=', number)

        #turning the binary dictionary into a list and then a string (broken up into 8bits for clarity).
        binary = ''
        bindictvalues = bindict.values()
        bit = 8
        for item in bindictvalues:
            if bit == 0:
                binary += ' ' + item
                bit = 8
            else:
                binary += item
                bit -= 1
                #print(bit)
        return binary

def printer(): # prints out the first value in the queue
    num = 1
    while t1.is_alive() or t2.is_alive():
        y = q.get()
        print(y, '=', sam_counter(y))
        num = num + 1


q = Queue(maxsize = 10)


if __name__ == '__main__':
  
    t1 = threading.Thread(target = randQ, args = (10,))
    t2 = threading.Thread(target = randQ, args = (10,))
    t3 = threading.Thread(target = printer)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    