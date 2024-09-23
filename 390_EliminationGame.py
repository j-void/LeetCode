class Solution:
    def lastRemaining(self, n: int) -> int:
        curr_length = n
        step = 1
        head = 1
        left = True

        while curr_length > 1:
            if left or curr_length % 2 != 0: ## skip when r->l and odd
                head = head + step
            curr_length = curr_length//2
            step = step * 2
            left = not left

        return head
