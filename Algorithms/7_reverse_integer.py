class Solution(object):
    def reverse(self, x):
        str_x = str(x)
        if str_x[0] == '-':
            new_str = [str_x[len(str_x) - i] for i in range(1, len(str_x))]
            output = int('-'+''.join(new_str))
            if output < (-pow(2,31)):
                output = 0
        else:
            new_str = [str_x[len(str_x) - i -1] for i in range(len(str_x))]
            output = int(''.join(new_str))
            if output > (pow(2,31)-1):
                output = 0
        return output
