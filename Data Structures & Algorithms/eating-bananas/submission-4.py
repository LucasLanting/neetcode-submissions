class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # maybe instead of guessing k = 1,2,3...
        # we should guess the median between the max and 1

        # obviously the upper bound answer is m which is max(piles)

        l,r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r)//2

            totalTime = sum([math.ceil(float(pile)/k) for pile in piles])
            if totalTime <= h:
                res = k
                # still check more to the left in 
                # case there is a better solution
                r = k - 1
            else:
                # search to the right, this value of k to small
                l = k + 1

        # note that if we go to the left and never find a better solution
        # we just return the best one we found before
        return res

            
