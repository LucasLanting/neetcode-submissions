# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# this is just binary search but instead of checking list[M] == target
# with M being the midpoint you search, you will guess M and use the
# guess(int num) function to tell you what to do next

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            m = (l+r)//2

            if guess(m) == 1:
                # guess is lower than the number. Search to the right
                l = m + 1
            elif guess(m) == -1:
                 # guess is higher than the number. Search to the left
                r = m - 1
            else:
                return m
                
        return -1   # didn't find the number
                