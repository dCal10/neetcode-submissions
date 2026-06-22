class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0] * n
        stack = []    #[temp, index]   
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                out = stack.pop()
                output[out[1]] = index - out[1]
            stack.append((temp, index))
        return output
                