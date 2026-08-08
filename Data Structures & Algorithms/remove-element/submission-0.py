class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        length = len(nums)
        while index<length:
            if nums[index]==val:
                nums.pop(index)
                length -= 1
            else:
                index += 1

        return length
        
