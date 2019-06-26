class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        days, memory = [0]*n, []
        memory.append(n-1)

        for i in range(n-2, -1, -1):
            while memory and T[memory[-1]] <= T[i]:
                memory.pop()
            days[i] = memory[-1] - i if memory else 0
            memory.append(i)
        return days 
