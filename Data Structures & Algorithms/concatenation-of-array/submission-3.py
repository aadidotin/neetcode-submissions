class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr_size = len(nums)
        array = [0] * (2 * arr_size)

        for i, v in enumerate(nums):
            array[i] = array[i + arr_size] = v

        return array