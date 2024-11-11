class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in bracket_map:
                # Pop from stack if stack is not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapped value doesn't match the popped value
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(char)
        
        # If the stack is empty, all brackets were matched properly
        return not stack





    



  

