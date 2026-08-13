class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sequence_map = {}
        for num in nums:
            if num not in sequence_map:
                sequence_map[num] = 1
        
        max_length = 1
        for key in sequence_map:
            # key is Starter
            if key-1 not in sequence_map:
                counter = 1
                current_key = key+1
                while current_key in sequence_map:
                    counter += 1
                    current_key += 1

                if counter>max_length:
                    max_length = counter

        return max_length


                 
        