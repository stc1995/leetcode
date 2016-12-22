# 1、想出来的现在草稿纸上写写步骤
# 2、如此题，可从people[i][0]或people[i][1]两个角度进行，若倾向的角度不行，不妨思考自己觉得不那么靠谱的角度
#
# 1.Pick out tallest group of people and sort them in a subarray (S). Since there's no other groups of people taller than them, therefore each guy's index will be just as same as his k value.
# 2.For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
# E.g.
# input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# subarray after step 1: [[7,0], [7,1]]
# subarray after step 2: [[7,0], [6,1], [7,1]]

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # 简化版
        res = []
        import itertools
        for k, g in itertools.groupby(sorted(people, reverse=True), key=lambda x : x[0]):
            #返回值k = 7,6,5,4  g是具有生成器性质的容器（sort、list一次就用完了），装的是[[7, 1], [7, 0]]\[[6, 1]]\[[5, 2], [5, 0]]\[[4, 4]]
            #可以看出:1,0 \2,0这样的数据也被排序了
            # print(type(k))
            # print(list(g))
            # print(list(sorted(g)))
            for person in sorted(g):
                # print(person)
                res.insert(person[1], person)
        return res

        # 原理讲清楚版
        # dict, height, res = {}, [], []
        #
        # for i in range(len(people)):
        #     p = people[i]
        #     if p[0] in dict:
        #         dict[p[0]] += (p[1], i),
        #         # dict[p(0)] += (p[1], i)
        #         # TypeError: 'list' object is not callable
        #     else:
        #         dict[p[0]] = [(p[1], i)] #不能写p(1), 要写p[1]
        #         height += p[0],
        #     # height += p[0],
        #     # TypeError: 'int'object is not iterable,要加逗号
        #
        # height.sort(reverse=True)
        #
        # for i in range(len(height)):
        #     h = dict[height[i]]
        #     h.sort()
        #     for j in range(len(h)):
        #         res.insert(h[j][0], people[h[j][1]])
        #
        # return res

s = Solution()
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(s.reconstructQueue(people))
