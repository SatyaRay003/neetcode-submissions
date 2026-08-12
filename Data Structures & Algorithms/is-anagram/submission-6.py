class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        s_map = {}
        for char in s:
            s_map[char] = s_map.get(char, 0) + 1
    
        for char in t:
            if char not in s_map:
                return False
            else:
                s_map[char] -= 1
                
            if s_map[char]==0:
                s_map.pop(char)

        if len(s_map)>0:
            return False

        return True