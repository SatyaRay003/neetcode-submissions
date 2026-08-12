class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        s_map = {}
        for char in s:
            if char in s_map:
                s_map[char] += 1
            else:
                s_map[char] = 1

        t_map = {}
        for char in t:
            if char in t_map:
                t_map[char] += 1
            else:
                t_map[char] = 1

        if len(s_map)!=len(t_map):
            return False

        for key in s_map:
            if key not in t_map:
                return False
            elif s_map[key]!=t_map[key]:
                return False

        return True

        