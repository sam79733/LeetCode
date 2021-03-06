"""Construct Binary Search Tree from Preorder Traversal


Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.


Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]


Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder = sorted(preorder)
        return self.costructBST(preorder, inorder)
    
    
    
    def costructBST(self, preorder, inorder):
        lenpreOrder = len(preorder)
        leninOrder = len(inorder)
        
        if lenpreOrder != leninOrder or lenpreOrder == None or leninOrder == None or lenpreOrder == 0:
            return None
        
        root = TreeNode(preorder[0])
        rootindex = inorder.index(root.val)
        
        root.left = self.costructBST(preorder[1:rootindex+1], inorder[:rootindex])
        
        root.right =  self.costructBST(preorder[rootindex+1:], inorder[rootindex+1:])
        
        return root
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        