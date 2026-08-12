class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(0, len(nums)):
            remain = target-nums[i] 
            if remain in hash_map:
                return [hash_map[remain][0], i]
            else:
                hash_map[nums[i]] = [i]
