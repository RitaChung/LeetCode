class Solution(object):
    def lengthOfLastWord(self, s):
        str_len = len(s)
        if s.count(' ') == str_len:
            return 0
        elif str_len == 1 and s != ' ':
            return 1
        else:
            count = 0
            last = ' '
            for i in range(1, str_len+1):
                if s[-i].isalpha():
                    last = s[-i]
                elif not s[-i].isalpha() and last == ' ':
                    count += 1
                    last = s[-1]
                elif not s[-i].isalpha() and last != ' ':
                    return i-1-count
        return i-count

