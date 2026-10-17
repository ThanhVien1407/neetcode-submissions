class Solution:
    def isValid(self, s: str) -> bool:

        bracket = {')': '(', '}': '{', ']': '['}
        stack = []  

        for i in s:

            if i in bracket:
                if len(stack) > 0:
                    pt = stack.pop()
                else:
                    pt = '#'
                if bracket[i] != pt:
                    return False
            else:
                stack.append(i)
                
        if not stack:
            return True

        else:
            return False
