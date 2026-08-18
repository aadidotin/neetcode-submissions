class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = {}

        for num in nums:
            major[num] = major.get(num, 0) + 1

        return max(major, key=major.get)