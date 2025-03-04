class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        read = False
        positive = True
        signed = False
        i = 0
        digits = ''

        while i < n:
            cur = s[i]
            i += 1
            if not read:
                if signed and (cur == '+' or cur == '-' or cur == ' '):
                    i = n
                    continue
                elif cur == ' ':
                    continue
                elif cur == '+':
                    signed = True
                elif cur == '-':
                    positive = False
                    signed = True
                elif cur.isdigit():
                    digits += cur
                    read = True
                else:
                    i = n
            else:
                if cur.isdigit():
                    digits += cur
                else:
                    i = n
        if len(digits) < 1:
            return 0
        num = int(digits)
        if positive and num > 2**31-1:
            return 2**31-1
        elif not positive and num > 2**31:
            return -2**31
        elif not positive:
            return -num
        else:
            return num
        return 0