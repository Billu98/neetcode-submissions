class Solution:
    def validAnagram(self, a: str, b:str) -> bool:
        
        countA = {}
        
        countB = {}
        
        for ch in a:
            
            countA[ch] = countA.get(ch, 0) + 1
        
        for ch in b:
            countB[ch] = countB.get(ch, 0) + 1
        
        return countA == countB
    
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        windowLength = len(s1)
        
        for i in range(len(s2) - windowLength + 1):
            
            window = s2[i: i + windowLength]
            
            if self.validAnagram(s1, window):
                return True
        return False
        
s1 = "abc"
s2 = "lecabee"
print(Solution().checkInclusion(s1, s2))