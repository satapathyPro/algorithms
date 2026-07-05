from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        var = list (count.items())
        
        var1 = sorted(var, key = lambda x: x[1], reverse =True)
        # sorted_items= sorted(count.items(),key= lambda pair: pair[1], reverse = True)
        ans = []
        for i in range(k):
            ans.append(var1[i][0])

        return ans
        #return [sorted_items[i][0] for i in range(k)]
        #return [pair[0] for pair in sorted_items[:k]]
        #return [x[0] for x in sorted_items[:k]]
        