class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict_s1 = {}

        if len(s1) > len(s2):
            return False
        
        arr = [0] * 26
        arr_s2 = [0] * 26

        for i in range(len(s1)):
            arr[ord(s1[i]) - ord('a')] += 1
            # build the fixed sliding window for s2    
            arr_s2[ord(s2[i]) - ord('a')] += 1

        if arr == arr_s2: 
            return True

        # go from the last ch in s1 to the end of the second string
        for i in range(len(s1), len(s2)): 
            arr_s2[ord(s2[i]) - ord('a')] += 1
            arr_s2[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if arr_s2 == arr: 
                return True
        return False

        