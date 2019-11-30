"""
Python Script to compute mean median mode of n numbers.
Input: <number of numbers>
       n1 n2 n3 .... nn
Output: mean value
        median value
        mode value
"""
number_of_inputs = int(input())
numbers = [int(n) for n in input().split()]
numbers.sort()
median = 0
if number_of_inputs % 2 == 0:
    median = (numbers[int(number_of_inputs/2)]+numbers[int(number_of_inputs/2)-1])/2
else:
    median = numbers[(number_of_inputs-1)/2]
mean = sum(numbers)/number_of_inputs
max_count = 0
index = 0
for num in numbers:
    count = numbers.count(num)
    if count > max_count:
        max_count = count
        index = numbers.index(num)
mode = numbers[index]
print(mean)
print(median)
print(mode)
