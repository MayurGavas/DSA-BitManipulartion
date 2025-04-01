def convertTobit(num):
    print(bin(num))
    print(format(num,'b'))
#convertTobit(6)

def printNumberOfFixedBits(num,noOfBits):
    print(format(num,f'0{noOfBits}b'))
#printNumberOfFixedBits(5,8)

def leftShift(num):  # Multiply by 2
    print(num, format(num, f'0{8}b'))
    num = num << 1
    print(num, format(num, f'0{8}b'))
    print(num)
#leftShift(20)

def rightShift(num): # Divide by 2
    print(num,format(num,f'0{8}b'))
    num = num >> 1
    print(num,format(num,f'0{8}b'))
    print(num)
#rightShift(20)

def leftShiftNTimes(num,i):    # Multiply by 2 ^ n
    print(num, format(num, f'0{8}b'))
    num = num << i
    print(num, format(num, f'0{8}b'))
    print(num)
#leftShiftNTimes(10,3)


def rightShiftNTimes(num,i):    # Divide by 2 ^ n
    print(num, format(num, f'0{8}b'))
    num = num >> i
    print(num, format(num, f'0{8}b'))
    print(num)
#rightShiftNTimes(100,3)

def flipAllBits(num):
    print(num, format(num, f'0{8}b'))
    num = ~num
    print(num, format(num, f'0{8}b'))
    print(num)
flipAllBits(5)

"""In Python, integers are stored using two’s complement representation, meaning:
Positive numbers are stored normally in binary.
Negative numbers are stored by flipping all bits and adding 1.
"""

#########################
# TODO :EASY FUNCTIONS
#########################
def is_odd(num):
    return (num & 1) == 1    # return True if ODD

def getIthBit(num,i):
    return (num >> i) & 1    # returns True if ith bit is set

def setIthBit(num,i):
    return num | (1 << i)

def clearIthBit(num,i):
    return num & ~(1 << i)

def toggleIthBit(num,i):
    return num ^ (1 << i)

def isPowerOf2(num):
    return num > 0 and (num & (num-1)) == 0

def countSetBits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

def swap(a,b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a,b


