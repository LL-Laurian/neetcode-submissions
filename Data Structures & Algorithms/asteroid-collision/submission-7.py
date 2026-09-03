class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        def noCollision(a, b):
            return ((a>0 and b >0) or (a<0 and b <0)) or (a>0 and b<0)

        for ast in asteroids:
            if stack == [] or noCollision(ast, stack[-1]):
                stack.append(ast)
            else:
                while stack and not noCollision(ast, stack[-1]) and abs(ast) > abs(stack[-1]):
                    stack.pop()

                if stack and (stack[-1]>0 and ast <0) and abs(ast) == abs(stack[-1]):
                    stack.pop()
                    continue
                elif stack == [] or noCollision(ast, stack[-1]):
                    stack.append(ast)

        return stack
                

    