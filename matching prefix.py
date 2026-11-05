def chooseSmallest (words)->str:
    smallest = words[0]
    for word in words:
        if len(word) < len(smallest):
            smallest = word
    return smallest


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res=""
        sm = chooseSmallest(strs)
        parts = self.getParts(sm)
        for part in parts:
            isIn = True
            for word in strs:
                if not word.startswith(part):
                    isIn = False
                    break
            if isIn:
                if len(part) > len(res):
                    res = part
        return res



    def getParts(self, word: str) -> list[str]:
        parts = []
        for i in range(len(word)):
            parts.append(word[:i + 1])
        return parts


    def chooseSmallest (words)->str:
        smallest = words[0]
        for word in words:
            if len(word) < len(smallest):
                smallest = word
        return smallest


print(Solution().longestCommonPrefix(["flower","flow","flight"]))
