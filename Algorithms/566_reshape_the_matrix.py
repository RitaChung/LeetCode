class Solution(object):
    def matrixReshape(self, nums, r, c):
        rows = len(nums)
        cols = len(nums[0])
        if rows * cols != r * c:
            return nums
        else:
            result = []
            temp = []
            for row in range(rows):
                for col in range(cols):
                    if len(temp) < c:
                        temp.append(nums[row][col])
                    else:
                        result.append(temp)
                        temp = []
                        temp.append(nums[row][col])
            result.append(temp)
            return result
