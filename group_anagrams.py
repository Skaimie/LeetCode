class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anag= {}
        for i in strs:
            b=list(i)
            b.sort()

            if str(b) in anag:
                anag[str(b)].append(i)
            else:
                anag[str(b)]=[i]

        return list(anag.values())


s= Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
