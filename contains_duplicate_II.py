class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d = {}

        for i, val in enumerate(nums):
            if val in d and i - d[val] <= k:
                return True

            d[val] = i

        return False
s=Solution()

print(s.containsNearbyDuplicate([1,2,3,1],0))
