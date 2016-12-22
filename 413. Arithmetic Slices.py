# 思路1：
# 若序列S为等差数列，其长度为N，则其等差数列切片的个数SUM = 1 + 2 + ... + (N - 2) <--------至少长为3
# 例如，等差数列[1, 2, 3, 4, 5, 6]的切片个数为1+2+3+4 = 10
# 这10个切片分别是：[1,2,3], [1,2,3,4], [1,2,3,4,5], [1,2,3,4,5,6][2,3,4], [2,3,4,5], [2,3,4,5,6][3,4,5], [3,4,5,6][4,5,6]
#
# 思路2：分解问题
# 如果是不连续的，如1231234，很明显123和1234两个是独立的，
# 如果知道了一个序列变得不连续了，也就是说P[n]-P[n-1]!=P[n-1]-P[n-2],那就说明这是两个独立的序列，需要分别计算，最后求和
# 所以问题可以简化成，如何求两个独立的等差片段
# 如何求一个以X结尾的连续的等差片段，它的子等差片段有多少个？
# 这个时候又可以从初始状态考虑起，先考虑只有三个的等差序列，只有1个slice，如果长度是4，就是1+2=3个，如果长度是5，就是又多出了3个，1+2+3=6个，原来是个Fibonacchi序列，这样的话就可以用动态规划的方法求出来了
# 用cur和sum保存已经求出来的和，一旦等差序列“断了”，就将cur清零


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # method 2
        if len(A) < 3:
            return 0
        res = 0
        cnt = 0
        delta = A[1] - A[0]
        for i in range(2, len(A)):
            if (A[i]-A[i-1]) == delta:
               cnt += 1
               res += cnt
            else :
                delta = A[i] - A[i-1]
                cnt = 0
        return res


        # method 1
        # res = 0
        # cnt = 0
        # if len(A) < 3:
        #     return 0
        # for i in range(2, len(A)):
        #     if (A[i-1]-A[i-2]) == (A[i]-A[i-1]):
        #        cnt += 1
        #        res += cnt
        #     else:
        #         cnt = 0
        # return res

s = Solution()
A = [1,2,3,4]
print(s.numberOfArithmeticSlices(A))
