class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        cur = ""
        res = ""
        num = 0
        stack = []
        while i < len(s):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i].isalpha():
                cur = cur + s[i]
            elif s[i] == '[':
                stack.append([cur, num])
                cur = ""
                num = 0
            elif s[i] == ']':
                prestr, curnum = stack.pop()
                cur = prestr + curnum*cur
            i += 1
        
        return cur