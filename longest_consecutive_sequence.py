class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num = set(nums)

        res=0
        while(len(num)>0):
            a=1
            i = num.pop()
            f=i
            while(True):
                if i+1 in num:
                    a+=1
                    i+=1
                    num.remove(i)
                else:break
            i=f
            while(True):
                if i-1 in num:
                    a+=1
                    i-=1
                    num.remove(i)
                else:break
            res = max (a,res)



        return res


s=Solution()
print(s.longestConsecutive([0,-1]))
