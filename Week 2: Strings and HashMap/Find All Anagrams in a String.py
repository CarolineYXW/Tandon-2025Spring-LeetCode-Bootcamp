class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        cntp = Counter(p)
        l = 0
        r = len(p)
        cnts = Counter(s[l:r])
        ret = []

        while r <= len(s):
            if cnts == cntp:
                ret.append(l)
            cnts[s[l]] -= 1
            l += 1
            r += 1
            if r <= len(s):
                cnts[s[r-1]] += 1

        return ret