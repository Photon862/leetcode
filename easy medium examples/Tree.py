
# invert a binary tree
# u can do BFS or DFS but this is Depth first search

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # check if there is root if not cancel whole function
        if not root: return None

        # swap left root and right root of the top root node
        root.left, root.right = root.right, root.left

        # do the same for left and right subtrees
        # these set the new top root as root.left or root.right and repeat the process
        self.invertTree(root.left)
        self.invertTree(root.right)

        # return the ORIGINAL root
        return root


# find max depth of binary tree

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if there is no root return 0 instantly
        if not root:
            return 0

        # loop the function for left and right subtrees and add + 1 each time
        # on top the if stops the function from looping forever
        return 1 + max(
            self.maxDepth(root.left), self.maxDepth(root.right)
          )



