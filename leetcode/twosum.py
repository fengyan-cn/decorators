# 第一次遍历是2+7，2+11,2+15
# 第二次遍历是7+11,7+15
# 第三次遍历是11+15
class Solution(object):
    def twosum(self, nums, target):
        for i, value1 in enumerate(nums):
            for j, value2 in enumerate(nums[i+1:]):
                if value1 + value2 == target:
                    return [i,i+j+1]

nums = [2, 7, 11, 15]
target = 9
sum = Solution()
print(sum.twosum(nums,target))