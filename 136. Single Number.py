class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = {}
        for i in nums:
            if i in b:
                b[i] = 2
            else:
                b[i] = 1

        for i in b:
            if b[i] == 1:
                res = i

        return res