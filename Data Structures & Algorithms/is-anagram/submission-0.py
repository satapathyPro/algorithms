from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = defaultdict(int)
        for ch in s:
            seen[ch] += 1

        for ch in t:
            seen[ch] -= 1
        
        # return all(v == 0 for v in seen.values())
        return not any(seen.values())