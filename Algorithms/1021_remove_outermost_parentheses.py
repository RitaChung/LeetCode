class Solution(object):
    def removeOuterParentheses(self, S):
        stack = []
        cut_point = []
        for item in range(len(S)):
            letter = S[item]
            if not stack:
                cut_point.append(item)
                stack.append(letter)
            elif stack[-1] != letter:
                stack.pop()
            else:
                stack.append(letter)
        output = ""
        for run in range(len(cut_point)):
            if run != len(cut_point)-1:
                start = cut_point[run] + 1
                end = cut_point[run+1] - 1
                output += S[start:end]
            else:
                start = cut_point[run] + 1
                end = len(S) - 1
                output += S[start:end]
        return output
