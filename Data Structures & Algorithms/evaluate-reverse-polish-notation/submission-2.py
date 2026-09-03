class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ["+", "-", "*", "/"]
        stack =[]

        for token in tokens:
            try:
                int(token)
                stack.append(int(token))
            except ValueError:
                if len(stack)<2:
                    return 0
                else:
                    v2 = stack.pop()
                    v1 = stack.pop()

                    if token == "+":
                        res = v1 + v2
                    elif token == "-":
                        res = v1 - v2
                    elif token == "*":
                        res = v1 * v2
                    elif token == "/":
                        res = v1 / v2
                stack.append(int(res))
        
        return int(stack[-1])
        
        