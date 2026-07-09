class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 0
        prod = 1
        for i in range(len(nums)):
            if (nums[i]==0):
                count+=1
            else:
                prod = prod * nums[i]
        if (count>1):
            return [0 for i in range(len(nums))]
        elif(count==1):
            return [prod if num == 0 else 0 for num in nums]
        else:
            return [prod//num for num in nums]
