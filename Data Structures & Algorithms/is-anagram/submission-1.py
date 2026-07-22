class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

s = "racecar"
t = "carrace"
print(Solution().isAnagram(s, t))

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}

        for ch in s:
            countS[ch] = countS.get(ch, 0) + 1
        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1
        return countS == countT
print(Solution2().isAnagram(s,t))