class Solution(object):
    def plusOne(self, digits):
        max_run = len(digits)
        ind = 1
        while ind <= max_run:
            if digits[-ind] + 1 == 10:
                digits[-ind] = 0
                ind += 1
            else:
                digits[-ind] = digits[-ind] + 1
                break
        if ind == max_run + 1:
            digits.insert(0,1)
        return digits
