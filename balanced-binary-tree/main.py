# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(root: TreeNode | None) -> int:
    if root is None:
        return 0

    return max(height(root.left), height(root.right)) + 1


def isBalanced(root: TreeNode | None) -> bool:
    if root is None:
        return True

    return (
        abs(height(root.left) - height(root.right)) <= 1
        and isBalanced(root.left)
        and isBalanced(root.right)
    )


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        return isBalanced(root)
