class Solution:
    def search(self, nums: list[int], target: int) -> int:
        run = True
        checking = [0,len(nums)-1]
        while(run):
            run = checking[1 ]-checking[0]!=0
            i = self.middle(checking)
            a =nums[i]
            if a>target:
                checking = [checking[0],i-1]
                if i ==0:
                    checking = [checking[0],checking[0]]
            elif a< target:
                checking = [i+1,checking[1]]
                if i+1==len(nums):
                    checking = [checking[1],checking[1]]
            else:
                return i
        return -1
    def middle(self, nums: list[int])->int:
        return (nums[1]+nums[0]+1)//2



s= Solution()
print(s.search([-1,0,3,5,9,12],13))
