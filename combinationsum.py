class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []

        def backtrack(remain, path, start):
            if remain == 0:
               
                results.append(list(path))
                return
            elif remain < 0:
                
                return

            for i in range(start, len(candidates)):
              
                path.append(candidates[i])
                
               
                backtrack(remain - candidates[i], path, i)
                
               
                path.pop()

        backtrack(target, [], 0)
        return results
