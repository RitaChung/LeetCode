class Solution(object):
    def isPalindrome(self, x):
        str_x = str(x)
        if str_x[0] == '-':
            return False
        else:
            new_str = [str_x[len(str_x) - i - 1] for i in range(len(str_x))]
            reverse_str = int(''.join(new_str))
            return x == reverse_str
