'''
A decimal to binary converter that uses the same technique as a grid on paper
for example 10

starting with the biggest value that is less than the starting number take that form the starting number and add
a 1 to that column, repeat with remaining values.


|dec|8|4|2|1|
|---|-|-|-|-|
|bin|1|0|1|0|

'''

import time


def sam_counter(number):
    import math

    number = int(number)
    print('start number =', number)
    onumber = number
    if number == 0:
        print(0)
    else:

        #use the log of the number to find out how many bits are required to express the number in binary.
        log = int(math.log2(number)) + 1
        columns = list(range(log))
        print('There will be ', len(columns), ' bits', int(len(columns) / 8) + 1, 'bytes') #reports the number of bits
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

def binary_divide(input):
    if input == 0:
        return '0'
    binary = ''
    while input:
        if input % 2 != 0:
                binary = '1' + binary
        else:
                binary = '0' + binary
        input = int(input / 2)

    return binary


decimal = int(input('Decimal number?'))

print('divide by two')
start = time.perf_counter()
print(binary_divide(decimal))
end = time.perf_counter()
print(end-start, '\n')

print("sam's method")
start = time.perf_counter()
print(sam_counter(decimal))
end = time.perf_counter()
print(end-start, '\n')

print('bin()')
start = time.perf_counter()
print(bin(decimal))
end = time.perf_counter()
print(end-start, '\n')
