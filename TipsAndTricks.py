
# Find the Rightmost set Bit
# This is a bit trick to isolate the rightmost set bit (i.e., the lowest bit where the two unique numbers differ).
# Because this bit is different between the two unique numbers, and we can use it to separate them into two different groups.
def rightmost_setbit(num):
    rightmost_setbit = num & -num
    return rightmost_setbit

def shift_functionality(num):  # Multiply by 2
    print(num, format(num, f'0{8}b'))

shift_functionality(0)
shift_functionality(1)
shift_functionality(0 << 5)
shift_functionality(0 >> 5)
shift_functionality(1 << 3)
shift_functionality(1 >> 5)

def Not_function(num):
    print(num, format(num, f'0{8}b'))

Not_function(2)    # normal positive integer
Not_function(~2)   # ~2  =  ~(0010) =  1101 = -(0010 + 1) = -(0011) = -3
Not_function(-2)   # -2  =  -(0010)
#TODO : negative nums will be in format 1101  positive will be 0010. ||| -n will just flip all the bits of n
"""   ~ num will also flip all the bits reading both are different
1. ~ num = the ~ will flip all numbers (ie 1101), but ow to read this. As it starts with 1 this is a negative number.
In Python -ve numbers are stored in 2 components ie. a) 1101 will become -(0010) b) 1 is second component , we need to add these both
so, -(0010 + 1) = -(0011) = -3 , this becomes binary representation of -3.  Hence ~2 is equivalent to -3
"""


