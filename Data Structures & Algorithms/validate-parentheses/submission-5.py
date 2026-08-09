class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pop_map = {"]": "[", "}": "{", ")":"("}
        for bracket in s:
            if len(stack)>0 and stack[-1]==bracket_pop_map.get(bracket):
                stack.pop()
            else:
                stack.append(bracket)

        return True if len(stack)==0 else False

        