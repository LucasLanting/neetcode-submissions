class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # this is perfect for binary search

        l,r = 0, len(nums) - 1      # left and right pointer

        # we guess the middle value is our target if not...
        # kill half of the search space
        while l <= r:
            m = (l+r)//2    # assuring floored division
            
            if nums[m] < target:
                # search to the right of the midpoint
                l = m+1
            elif nums[m] > target:
                # search to the left of the midpoint
                r = m-1
            else:
                # we found it... nums[m] = target
                return m
        return -1
        
