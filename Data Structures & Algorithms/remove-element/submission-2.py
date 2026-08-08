class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        length = len(nums)
        while count<length:
            if nums[count]==val:
                nums.pop(count)
                length -= 1
            else:
                count += 1
        return length
        
        