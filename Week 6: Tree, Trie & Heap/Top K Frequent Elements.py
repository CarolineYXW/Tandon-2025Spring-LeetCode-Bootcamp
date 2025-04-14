class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ndic = {}
        for n in nums:
            try:
                 ndic[n] += 1
            except:
                ndic[n] = 1
        countdic = {}
        for n, count in ndic.items():
            try:
                countdic[count].append(n)
            except:
                countdic[count] = [n]
        ret = []
        frequency = countdic.keys()
        frequency.sort()
        for count in frequency[::-1]:
            if k >= len(countdic[count]):
                ret.extend(countdic[count])
                k -= len(countdic[count])
                if k <= 0:
                    return ret
            else:
                ret.extend(countdic[count][:k])
                return ret