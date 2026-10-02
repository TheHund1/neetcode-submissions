class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_count = 0
        result = 0
        was_previous_one = False
        for num in nums:
            if num == 1:
                if was_previous_one:
                    current_count += 1
                else:
                    was_previous_one = True
                    current_count = 1
                if current_count > result:
                    result = current_count
            else:
                was_previous_one = False
        return result