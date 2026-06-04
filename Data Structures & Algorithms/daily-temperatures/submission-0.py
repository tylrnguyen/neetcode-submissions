class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []


        # [30,38,30,36,35,40,28]

        # [1,4,1,2,1,0,0]

        # stk = [0]
        for i in range(len(temperatures)): 
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j

            stack.append(i)

        return result