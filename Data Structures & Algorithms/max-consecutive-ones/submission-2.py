class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        highest_count = 0
        counter = 0
        for number in nums:
            if number == 1:
                counter += 1
            else:
                counter = 0
            if counter > highest_count:
                highest_count = counter
        return max(highest_count, counter)
            