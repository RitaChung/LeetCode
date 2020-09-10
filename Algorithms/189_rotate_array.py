class Solution(object):
    def rotate(self, nums, k):
        for i in range(k):
            digit = nums.pop()
            nums.insert(0,digit)

