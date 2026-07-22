class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

s = "racecar"
t = "carrace"
print(Solution().isAnagram(s, t))