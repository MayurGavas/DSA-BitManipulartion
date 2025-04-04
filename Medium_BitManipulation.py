
# Finding the only non repeating element in array
def find_single(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Find two non repeating elements in array
def find_two_non_repeating_elements(nums):
    xor = 0
    for num in nums:
        xor ^= num

    rightmost_setbit = xor & -xor
    a = b = 0
    for num in nums:
        if num & rightmost_setbit:
            a ^= num
        else:
            b ^= num
    return a,b

# Find missing number in 0 to n
def find_missing(nums):
    n = len(nums)
    xor_all = 0
    xor_arr = 0
    for i in range(n+1):
        xor_all ^= i
    for num in nums:
        xor_arr ^= num

    return xor_all ^ xor_arr

# Find duplicate number in array
# Here for dup each bit is set whenever there is a unique number - called bitmasking
def find_duplicate(nums):
    dup = 0
    for num in nums:
        if (dup >> num) & 1:
            return num
        dup |= (1 << num)

# Find unique element where all elements appear 3 times
# This is classic example of thrice duplicates- in this code when the same element is traversed 3 times both one and two will become 0 once again
def find_unique_in_thrice(nums):
    one, two = 0,0
    for num in nums:
        one = (one ^ num) & ~two
        two = (two ^ num) & ~one
    return one

# Reverse bits of a number -- first bit wil go last,last will come first
def reverse_bits(num, bits = 32):
    res = 0
    for _ in range(bits):
        res <<= 1
        res |= num & 1
        num >>= 1
    return res

