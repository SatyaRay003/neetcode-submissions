class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pop_map = {"]": "[", "}": "{", ")":"("}
        length = 0
        for bracket in s:
            if bracket in bracket_pop_map:
                if stack and stack[-1]==bracket_pop_map.get(bracket):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return True if not stack else False

        