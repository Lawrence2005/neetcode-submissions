class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)
            if token in ['+', '-', '*', '/']:
                right = int(stack.pop())
                left = int(stack.pop())

                if token == '+':
                    result = left + right
                elif token == '-':
                    result = left - right
                elif token == '*':
                    result = left * right
                else:
                    result = int(left / right)
                stack.append(result)
            else:
                stack.append(token)
        
        return int(stack[-1])