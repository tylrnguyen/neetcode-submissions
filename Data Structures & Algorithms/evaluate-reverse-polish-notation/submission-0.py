class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for c in tokens: 
            if c == "+":
                a = stk.pop()
                b = stk.pop()
                stk.append(a + b)
            elif c == "*": 
                a = stk.pop()
                b = stk.pop()
                stk.append(a * b)
            elif c == "-":
                a = stk.pop()
                b = stk.pop()
                stk.append(b - a)
            elif c == "/":
                a = stk.pop()
                b = stk.pop()
                stk.append(int(float(b) / a))
            else:
                stk.append(int(c))
        return stk[-1]