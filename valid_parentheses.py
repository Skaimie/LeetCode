class Solution:
    def isValid(self, s: str) -> bool:
        res = True
        ind = self.get_pos(s)
        parts = self.get_parts(ind,s)
        for part in parts:
            if not res:
                return False
            res = res and self.check(part)

            new = part[1:-1]
            if new != "":
                res = res and self.isValid(new)

        return res

    def get_ins(self, n:int, s:str):
        opens = 1
        now = s[n]
        close = ")" if now == "(" else "]"if now=="[" else "}"
        output = ""
        for i in range(n+1,len(s)):
            if s[i]==now:
                opens+=1
            elif s[i]==close:
                opens-=1
            if opens == 0:
                break
            output+=s[i]
        return output
    def get_pos(self,s:str)-> list[int]:
        res = [0]
        opens = 0

        for i in range(len(s)):
            now = s[res[-1]]
            close = ")" if now == "(" else "]"if now=="[" else "}"
            if s[i]==now:
                opens+=1
            elif s[i]==close:
                opens-=1
            if opens == 0 and i < len(s)-1:
                res.append(i+1)
        return res
    def check(self,s:str)-> bool:
        if s=="":
            return True
        pr = s.count("(")== s.count(")")
        br = s.count("[")== s.count("]")
        cu = s.count("{")== s.count("}")
        op = True if (s[0]=="(" and s[-1]==")")or (s[0]=="{" and s[-1]=="}") or (s[0]=="[" and s[-1]=="]") else False

        return pr and br and cu and op
    def get_parts(self, indexes:list[int],s)-> list[str]:
        res = []
        for i in range(len(indexes)):
            if i+1==len(indexes):
                res.append(s[indexes[i]:])
                break
            res.append(s[indexes[i]:indexes[i+1]])


        return res






s= "[()]()"
x = Solution()
indexes = x.multi_check(s)
print(indexes)
# for i in range(len(indexes)):
#     if i+1==len(indexes):
#         print(s[indexes[i]:])
#         break
#     print(s[indexes[i]:indexes[i+1]])
