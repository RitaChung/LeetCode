class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        if strs == []:
            return ''
        else:
            str1 = strs[0]
            str2 = strs[-1]
            run = 0
            if len(str1) < len(str2):
                while run < len(str1):
                    if str1[run] != str2[run]:
                        break
                    run += 1
                return str1[:run]
            else:
                while run < len(str2):
                    if str1[run] != str2[run]:
                        break
                    run += 1
                return str2[:run]

