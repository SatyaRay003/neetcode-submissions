class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        max_length=1
        counter=1
        for i in range(0, len(nums)-1):

            if nums[i]==nums[i+1]:
                pass
            elif nums[i]+1==nums[i+1]:
                counter += 1
            else:
                if counter>max_length:
                    max_length = counter
                counter=1

        if counter>max_length:
            max_length = counter

        return max_length

            
        