class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_obj = {}
        t_obj = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_obj[s[i]] = s_obj.get(s[i], 0) + 1
            t_obj[t[i]] = t_obj.get(t[i], 0) + 1

        return s_obj == t_obj
        