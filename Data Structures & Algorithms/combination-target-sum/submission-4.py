class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, cursum, combination):
            if index == len(nums):
                return
            if cursum > target:
                return
            if cursum == target:
                res.append(combination)
                return
            dfs(index, cursum + nums[index], combination + [nums[index]])
            dfs(index + 1, cursum, combination)
  
        dfs(0, 0, [])
        return res