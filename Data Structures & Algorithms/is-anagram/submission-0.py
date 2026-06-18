class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        str1 = {}
        for ch in s: 
            # for each character, add 1 to occurences
            str1[ch] = str1.get(ch, 0) + 1
        
        for ch in t: 
            # if ch isn't in hash table, or no more occurences
            if ch not in str1 or str1[ch] == 0:
                return False 
            str1[ch] -= 1

        return True
