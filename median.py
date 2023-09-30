"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

numbers.sort()

def findMedian(nums):
    if len(nums)%2 == 1:
        # return number in middle of list
        return nums[(len(nums)//2)]
    else:
        # return mean on the 2 numbers in middle of list
        return (nums[int(len(nums)/2-1)] + nums[int(len(nums)/2)])/2
    
print(findMedian(numbers))