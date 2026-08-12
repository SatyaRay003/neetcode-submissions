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

        for char in t:
            if char in s_map:
                s_map[char] -= 1
            else:
                s_map[char] = 1

            if s_map[char]==0:
                s_map.pop(char)

        if len(s_map)>0:
            return False

        return True