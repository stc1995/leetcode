# 1、求从开始到某一个点的，考虑下之前算的成果有用吗？看看能不能用递推
# 2、若变动的情况少或者引起的可能变化就几个，列一列找找规律

import math

class solution(object):
    def countBits(self, num):
        # S4  递推式：ans[n] = ans[n & (n - 1)] + 1
        ans = [0]
        for i in range(1, num+1):
            ans += ans[i & (i-1)] + 1,
        return ans


        # S3  递推式：ans[n] = ans[n - highbits(n)] + 1
        # highbits运算可以不必每次都执行，用变量pow记录当前数字i的highbits；当i == pow时，令pow左移一位
        # ans = [0]
        # pow = 1
        # for i in range(1, num+1):
        #     ans += ans[i - pow] + 1,
        #     pow  = pow << (i == (pow))
        # return ans

        #  S2  递推式：ans[n] = ans[n - highbits(n)] + 1
        #              highbits(n) = 1<<int(math.log(x,2))
        # ans = [0]
        # for i in range(1, num+1):
        #     ans += ans[i - (1 << int(math.log(i, 2)))] + 1,
        # return ans


        #  S1  递推式：ans[n] = ans[n >> 1] + (n & 1)
        # ans = [0]
        # for i in range(1, num+1):
        #     ans += ans[i >> 1] + (i&1),
        # return ans

so = solution()
num = 5
print(so.countBits(num))



