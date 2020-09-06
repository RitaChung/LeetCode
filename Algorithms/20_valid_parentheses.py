iclass Solution(object):
    def isValid(self,s):
        list_s = list(s)
        symbol = {'{':{'action':'push','code':1},
                  '}':{'action':'pop','code':1},
                  '[':{'action':'push','code':2},
                  ']':{'action':'pop','code':2},
                  '(':{'action':'push','code':3},
                  ')':{'action':'pop','code':3}}
        if len(list_s) % 2 != 0:
            return False
        else:
            stack = []
            for run in range(len(list_s)):
                if symbol[list_s[run]]['action'] == 'push':
                    stack.append(symbol[list_s[run]]['code'])
                else:
                    if not stack:
                        return False
                    else:
                        pop_out = stack.pop()
                        if symbol[list_s[run]]['code'] != pop_out:
                            return False
            if not stack: # None == False == []
                return True
