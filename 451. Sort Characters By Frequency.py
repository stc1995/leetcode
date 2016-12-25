class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # method 2
        import collections
        return ''.join(i*j for i,j in collections.Counter(s).most_common())

        # method 1
        # s_list = list(s)
        # s_list.sort()
        # s = {}
        # keys = []
        # cnt = 1
        # i = 0
        # res = ''
        #
        # length = len(s_list)
        # while i < length:
        #     cur = s_list[i]
        #     while (i+cnt) < length and cur == s_list[i+cnt]:
        #         cnt += 1
        #     if cnt in s:
        #         s[cnt] += cur,
        #     else:
        #         s[cnt] = [cur]
        #         keys.append(cnt)
        #     i = i + cnt  # 注意
        #     cnt = 1      # 前后顺序
        #
        # keys.sort(reverse=True)
        # for i in keys:
        #     for j in s[i]:
        #             res += j*i #############
        # return res

# Time Limit Exceeded
# class Solution(object):
#     def frequencySort(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         s_list = list(s)
#         s_list.sort()
#         s = {}
#         keys = []
#         cnt = 1
#         i = 0
#         res = ''
#
#         length = len(s_list)
#         while i < length:
#             cur = s_list[i]
#             while (i+cnt) < length and cur == s_list[i+cnt]:
#                 cnt += 1
#             if cnt in s:
#                 s[cnt] += cur,
#             else:
#                 s[cnt] = [cur]
#                 keys.append(cnt)
#             i = i + cnt
#             cnt = 1
#
#         keys.sort(reverse=True)
#         for i in keys:
#             for j in s[i]:
#                 counting = i
#                 while counting > 0:
#                     res += j
#                     counting -= 1
#         return res

sol = Solution()
s = "tree"
print(sol.frequencySort(s))