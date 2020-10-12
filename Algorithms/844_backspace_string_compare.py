class Solution(object):
    def backspaceCompare(self, S, T):
        S_stack = []
        T_stack = []
        for s in range(len(S)):
            if S[s] == '#':
                if S_stack != []:
                    S_stack.pop()
            else:
                S_stack.append(S[s])
        for t in range(len(T)):
            if T[t] == '#':
                if T_stack != []:
                    T_stack.pop()
            else:
                T_stack.append(T[t])

        return ''.join(S_stack) == ''.join(T_stack)

