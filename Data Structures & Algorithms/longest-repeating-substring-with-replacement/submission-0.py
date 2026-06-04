from collections import defaultdict 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # initialize a dictionary to keep track of letter occurences 
        count = defaultdict(int)
        # maximum substring
        max_length = 0
        # character most occuring
        max_freq = 0

        l = 0
        r = 0

        while r < len(s): 
            # add the character to the dictionary
            # check if the character you added has max freq
            # check length of the substring
            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])

            while r - l + 1 > max_freq + k: 
                count[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
            r += 1 
        return max_length
