class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 1, 1
        ans = [1] * len(nums)
        ans[0] = nums[0]
        for i in range(len(nums)):
            ans[i] = left
            left *= nums[i]
        for j in reversed(range(len(nums))):
            ans[j] *= right
            right *= nums[j]
        return ans