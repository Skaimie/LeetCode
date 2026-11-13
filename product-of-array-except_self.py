
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prod = 1
        res=[]
        zero = -1
        zeros = 0
        for i,val in enumerate(nums):
            if val !=0:
                prod*=val
            else:
                zero=i
                zeros+=1
        if zeros >1:
            res = [0]*len(nums)
            return res

        elif zero!=-1:
            res = [0]*len(nums)
            res[zero] = prod
            return res
        res = [prod//n for n in nums]
        return res
