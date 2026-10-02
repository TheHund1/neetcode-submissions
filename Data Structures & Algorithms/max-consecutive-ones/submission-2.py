class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_count = 0
        result = 0
        for num in nums:
            if num == 1:
                if current_count > 0:
                    current_count += 1
                else:
                    current_count = 1
                if current_count > result:
                    result = current_count
            else:
                current_count = 0
        return result