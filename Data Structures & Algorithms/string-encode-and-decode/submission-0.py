class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs: 
            encoded_string += str(len(s)) + "#" + s
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        while i < len(s): 
            j = i

            while s[j] != "#":
                j += 1

            s_len = int(s[i:j])

            word_start = j + 1
            word = s[word_start : word_start + s_len]

            decoded_strs.append(word)

            i = word_start + s_len
        
        return decoded_strs



