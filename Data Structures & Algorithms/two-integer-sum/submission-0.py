class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            required = target - num
            if seen.get(required) != None:
                return [seen[required], i]
            seen[num]=i
        return [] 