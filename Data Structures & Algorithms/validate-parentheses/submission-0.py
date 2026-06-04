class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        str_map = { ")" : "(", "]" : "[", "}" : "{"}

        for i in s: 
            if i in str_map: 

                if stk and stk[-1] == str_map[i]:
                    stk.pop()
                else:
                    return False 
            
            else:
                stk.append(i)
            
        return True if not stk else False