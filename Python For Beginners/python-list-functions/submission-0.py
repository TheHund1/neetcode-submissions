from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    res = 0
    for num in nums:
        res += num
    return res

def get_min(nums: List[int]) -> int:
    res = nums[0]
    for i in range(1, len(nums)):
        if res > nums[i]:
            res = nums[i]
    return res

def get_max(nums: List[int]) -> int:
    res = nums[0]
    for i in range(1, len(nums)):
        if res < nums[i]:
            res = nums[i]
    return res

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
