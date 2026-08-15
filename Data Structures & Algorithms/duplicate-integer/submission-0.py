class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_contain = {}
        for x in nums:
            if dup_contain.get(x):
                return True

            dup_contain[x] = 1
        
        return False