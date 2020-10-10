class Solution(object):
    def removeDuplicates(self, S):
        stack = []
        for item in range(len(S)):
            letter = S[item]
            if stack == []:
                stack.append(letter)
            elif stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)

