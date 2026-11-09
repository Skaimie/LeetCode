class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        num1={}
        num2={}
        s1=set()
        s2=set()
        a=0
        for i in nums1:
            if i in s1:
                num1[i]+=1
            else:
                num1[i]=1
                s1.add(i)
        for i in nums2:
            if i in s2:
                num2[i]+=1
            else:
                num2[i]=1
                s2.add(i)


        sames = s1&s2
        for i in sames:
            res+=[i]*(min(num1[i],num2[i]))

        return (res)

