class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder, stack = preorder.split(","), []
        for node in preorder:
            # print(node,stack)
            while stack and node == stack[-1] == "#":
                stack.pop()
                if not stack:  return False
                stack.pop()
            stack.append(node)
        return stack == ["#"]