# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if len(set(t))!=len(set(s)) or len(s)!= len(t):
#             return False
#         sTup = []
#         tTup = []
#         for i in range(len(s)):
#             if s[i] in sTup:
#                 a= sTup.index(s[i])
#                 if t[i]!=tTup[a]:
#                     return False
#             else:
#                 sTup.append(s[i])
#                 tTup.append(t[i])
#         return True




###############

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(t))!=len(set(s)):
            return False
        n=set()
        for i in range(len(s)):
            n.add((s[i],t[i]))
        return len(n)==min(len(set(t)),len(set(s)))



s = Solution()


print(s.isIsomorphic("tititi","bobobo"))
