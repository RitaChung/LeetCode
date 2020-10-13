class Solution(object):
    def makeGood(self, s):
        stack = []
        for item in range(len(s)):
            letter =  s[item]
            if not stack:
                stack.append(letter)
            elif stack[-1].islower() and stack[-1].upper() == letter:
                stack.pop()
            elif stack[-1].isupper() and stack[-1].lower() == letter:
                stack.pop()
            else:
                stack.append(letter)
        return "".join(stack)
