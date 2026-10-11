class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(start, path, remaining_target):
            if remaining_target == 0:
                result.append(path[:])
                return
            if remaining_target < 0:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, remaining_target - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return result