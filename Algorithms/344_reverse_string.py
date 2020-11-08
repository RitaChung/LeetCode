class Solution(object):
    def reverseString(self, s):
        for item in range(int(len(s) / 2)):
            inter = s[item]
            s[item] = s[-(item + 1)]
            s[-(item + 1)] = inter
