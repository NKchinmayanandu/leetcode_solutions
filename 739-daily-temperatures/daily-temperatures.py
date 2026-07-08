class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        result = [0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while answer:
                if temp > temperatures[answer[-1]]:
                    result[answer[-1]] = i-answer[-1]
                    answer.pop(-1)
                else:
                    break
            answer.append(i)
        return result