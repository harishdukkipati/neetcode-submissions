#Understand
# create a new array that for each index inputs the amount of time you need to wait till you see an index with a greater temperature

# Plan 
# sliding window 
# iterate through temperatures
# res = []
# for i in range(len(temperatures))
# k = 0 
# j = i + 1
# while j < len(temperatures) and temperatures[j] <= temperatures[i]
# k += 1
# j += 1
# if j == len(temperatures) or k == 0:
# k = 0
# res.append(k)
# res.append(k+1)
# return res

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            k = 0
            j = i + 1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                k += 1
                j += 1
            if j == len(temperatures):
                k = 0
                res.append(k)
            else:
                res.append(k+1)
        
        return res