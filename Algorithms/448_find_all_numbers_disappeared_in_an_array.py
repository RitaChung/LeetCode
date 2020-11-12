class Solution(object):
    def findDisappearedNumbers(self, nums):
        uni_num = set(nums)
        full_num = set(range(1,len(nums)+1))
        return list(full_num-uni_num)
