class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_list = list(s)
        t_list = list(t)

        for i in range(len(s_list)):
            if s_list[i] in t_list:
                t_list.remove(s_list[i])

        res = ''.join(t_list)
        return res
