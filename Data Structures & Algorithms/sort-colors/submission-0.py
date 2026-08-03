class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Use bucket sort! Here we have 3 buckets 0,1,2

        counts = [0]*3
        # first pass through array to get counts
        for num in nums:
            counts[num] += 1    # the index is simply the number here
        
        # second pass through to now change nums to have those counts in order
        i = 0   # ptr to which part of array we are at
        for n in range(len(counts)):
            for j in range(counts[n]):
                nums[i] = n
                i += 1
        return
