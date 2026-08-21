class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouping = {}

        for _str in strs:
            count = [0] * 26

            for char in _str:
                index = ord(char) - ord('a')
                count[index] += 1

            s_str = tuple(count)
            
            if s_str not in grouping:
                grouping[s_str] = []

            grouping[s_str].append(_str)

        return list(grouping.values())
