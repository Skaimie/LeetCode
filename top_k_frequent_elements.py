class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        a={}
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        d= dict(sorted(a.items(), key=lambda x: x[1],reverse=True))
        return [list(d.keys())[n] for n in range(k)]
s=Solution()
print(s.topKFrequent([4,1,-1,2,-1,2,3],2))
