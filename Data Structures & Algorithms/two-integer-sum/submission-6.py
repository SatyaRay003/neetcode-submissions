class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            remain = target-num
            if remain in hash_map:
                return [hash_map[remain], i]
            hash_map[num] = i
