class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1.copy()

        # two pointers to each list (nums1_copy) and nums2
        p1 = 0
        p2 = 0 
        i = 0
        while i < m+n: 
            if (p2 >= n):
                nums1[i] = nums1_copy[p1]
                p1 += 1
            elif (p1 == m) or (nums1_copy[p1] > nums2[p2]):
                nums1[i] = nums2[p2]
                p2 += 1
            else:
                nums1[i] = nums1_copy[p1]
                p1 += 1
            i+= 1

