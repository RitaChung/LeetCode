class Solution(object):
    def firstUniqChar(self, s):
        dic = {}
        indix = len(s)-1
        for chr in s:
            if chr not in dic.keys():
                dic[chr] = 1
            else:
                dic[chr] += 1
        for chr in dic.keys():
            if dic[chr] == 1:
                if s.index(chr) < indix:
                    indix = s.index(chr)
        if 1 not in dic.values():
            indix = -1
        return indix
