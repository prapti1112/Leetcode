class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = [] # [[temperature, index]]
        
        for curr_ind, curr_temp in enumerate(temperatures):
            while stack and curr_temp > stack[-1][0]:
                stack_temp, stack_ind = stack.pop()
                answer[stack_ind] = curr_ind - stack_ind
            
            stack.append([curr_temp, curr_ind])
            
        return answer