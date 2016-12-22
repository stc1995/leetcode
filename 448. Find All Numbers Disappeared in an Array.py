# 一般有O(n)这样空间、时间复杂度限制的题，就不能用built-in function
# 此题运用了len(nums) = max(修复后的nums) 这个联系


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            nums[abs(n)-1] = -abs(nums[abs(n) - 1])
        return [i + 1 for i,n in enumerate(nums) if n > 0]
        ###########################################此处用[]
        # 若用return (),则返回 < generator object Solution.findDisappearedNumbers. < locals >.< genexpr > at 0x000002C59F44AD00 >

        # runtime limit
        # ans = []
        # min_nums = min(nums)
        # max_nums = max(nums)
        # for i in range(min_nums,max_nums+1):
        #     if i in nums:
        #        pass
        #     else:
        #        ans.append(i)
        # return ans

s = Solution()
nums =  [4,3,2,7,8,2,3,1]
print(s.findDisappearedNumbers(nums))
