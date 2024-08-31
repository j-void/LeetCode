class TreeNode:
    def __init__(self, val, left, right, left_child, right_child):
        self.val = val
        self.left = left
        self.right = right
        self.left_child = left_child
        self.right_child = right_child

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.root = self.build(0, len(nums)-1)
        

    def build(self, left, right):
        if left == right:
            return TreeNode(self.nums[left], left, left, None, None)
        mid = (left+right)//2
        left_child = self.build(left, mid)
        right_child = self.build(mid+1, right)
        return TreeNode(left_child.val+right_child.val, left, right, left_child, right_child)



    def update(self, index: int, val: int) -> None:
        def helper(node):
            if node.left == node.right:
                node.val = val
                return
            mid = (node.left+node.right)//2
            if index <= mid:
                helper(node.left_child)
                node.val = node.left_child.val + node.right_child.val
            else:
                helper(node.right_child)
                node.val = node.left_child.val + node.right_child.val

        helper(self.root)

    def sumRange(self, left: int, right: int) -> int:
        
        def helper(node, left, right):
            if node.left == left and node.right == right:
                return node.val
            mid = (node.left + node.right) // 2
            if right <= mid:
                return helper(node.left_child, left, right)
            elif left > mid:
                return helper(node.right_child, left, right)
            else:
                return helper(node.left_child, left, mid) + helper(node.right_child, mid + 1, right)
        return helper(self.root, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
