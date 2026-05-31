class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}

        # make two dict, check them against each other

        for i in s: 
            if i not in s1:
                s1[i] = 1
            else:
                s1[i] += 1
        
        for i in t:
            if i not in s2: 
                s2[i] = 1
            else: 
                s2[i] += 1

        if s1 == s2: 
            return True
        return False