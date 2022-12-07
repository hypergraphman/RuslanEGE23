from itertools import product

alf = '012345678'
nums = set()
for digits in product(alf, repeat=7):
    if (digits[0] != '0' and digits.count('6') == 1 and
       digits.count('1') + digits.count('3') +
       digits.count('5') + digits.count('7') == 2):
        nums.add(digits)
print(len(nums))
