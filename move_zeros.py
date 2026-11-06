from tkinter.constants import S


class Solution:
    def moveZeroes(self, nums: list[int]) -> list:
        """
        Do not return anything, modify nums in-place instead.
        """
        a= 0
        while(a<len(nums)):
            i=a
            if nums[a]==0:
                while(nums[i]==0and i<len(nums)-1):
                    i+=1
                n=nums[i]
                nums[a]=nums[i]
                nums[i]=0
            a+=1
        return nums


s=Solution()
print(s.moveZeroes([0,0,0,0,0,0,1,2,5,456,456,4,21,45,1,8,65,456,45,6,65]))
