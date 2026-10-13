class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        buckets = [0] * (len(nums) + 1)
        result = []
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        for num, count in counter.items():
            if buckets[count] == 0:
                buckets[count] = [num]
            else:
                buckets[count].append(num)
        for i in reversed(range(len(buckets))):
            if buckets[i] != 0:
                for num in buckets[i]:
                    result.append(num)
                    if len(result) == k:
                        return result
                
        