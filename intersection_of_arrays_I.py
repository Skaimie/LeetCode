class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        num1 = set(nums1)
        num2 = set(nums2)
        for i in num1:
            if i in num2:
                res.append(i)
        return res