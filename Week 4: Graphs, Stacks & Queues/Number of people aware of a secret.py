class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        forget_stack = [0] * (forget-1) + [1]
        share_stack = [0] * (delay-1) + [1]
        forget_sum, share_sum = 1, 1
        for i in range(n-1):
            forget_sum -= forget_stack.pop(0)
            share_sum -= share_stack.pop(0)
            new = forget_sum - share_sum
            forget_sum += new
            share_sum += new
            share_stack.append(new)
            forget_stack.append(new)
        return forget_sum % (10**9+7)