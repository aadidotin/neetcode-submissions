class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = strs[0]

        for i in range(1, len(strs)):
            common = []
            for j in range(len(prefix)):
                if j >= len(strs[i]) or prefix[j] != strs[i][j]:
                    break

                common.append(strs[i][j])

            prefix = "".join(common)
        
        return prefix
