class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        array = [0] * len(nums) * 2

        for i, v in enumerate(nums):
            array[i] = array[i + len(nums)] = v

        return array