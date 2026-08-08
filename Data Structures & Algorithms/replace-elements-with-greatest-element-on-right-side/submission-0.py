class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        for i in range(length):
            if i==length-1:
                arr[i]=-1
            else:
                max = 0
                for j in range(i+1, length):
                    if arr[j]>max:
                        max=arr[j]
                arr[i]=max

        return arr

        
