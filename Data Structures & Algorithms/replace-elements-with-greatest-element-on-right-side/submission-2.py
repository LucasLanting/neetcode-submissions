class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = arr[-1]
        arr[-1] = -1

        for i in reversed(range(len(arr)-1)):
            temp = arr[i]
            arr[i] = max_val
            max_val = max(max_val, temp)
        
        return arr



        