class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pop_map = {"]": "[", "}": "{", ")":"("}
        length = 0
        for bracket in s:
            if len(stack)>0 and stack[-1]==bracket_pop_map.get(bracket):
                stack.pop()
                length -= 1
            else:
                stack.append(bracket)
                length += 1

        return True if length==0 else False

        
