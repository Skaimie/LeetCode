class Solution:
    def firstUniqChar(self, s: str) -> int:
        res=[]
        no=[]
        for i in s:

            if i in no:
                continue
            elif i in res:
                res.remove(i)
                no.append(i)
            else:
                res.append(i)
        if len(res)!=0:
            return s.find(res[0])
        else:
            return -1
s= Solution()
print(s.firstUniqChar("loveleetcode"))


##Using sets will make it much faster
