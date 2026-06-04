class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                print(stack)
                right = stack.pop()
                left = stack.pop()

                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "/":
                    stack.append(int(left/right))
                else:
                    stack.append(right * left)
            else:
                stack.append(int(token))

        return stack[-1]