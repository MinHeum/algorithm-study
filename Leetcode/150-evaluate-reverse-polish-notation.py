class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque

        # 후위 연산 표기법
        stack = deque()

        for token in tokens:
            # 숫자면 stack에 넣기
            if token not in "+-*/":
                stack.append(int(token))
            # 연산자면 stack에서 숫자 두개 꺼내서 연산
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))

        return stack.pop()
