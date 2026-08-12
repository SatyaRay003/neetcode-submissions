class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_map = {}
        for num in nums:
            if num in unique_map:
                return True
            unique_map[num] = 1
        return False
        