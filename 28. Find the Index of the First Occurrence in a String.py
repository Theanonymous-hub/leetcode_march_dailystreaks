class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        m = len(haystack)
        if n > m:
            return -1
        if n == 0:
            return 0
        for firstIndex in range(m - n + 1):
            match = True
            for currIndex in range(n):
                if haystack[firstIndex + currIndex] != needle[currIndex]:
                    match = False
                    break
            if match == True:
                return firstIndex
        return -1
