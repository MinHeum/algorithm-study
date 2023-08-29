class Solution:
    def reverse(self, x: int) -> int:
        is_minus = False
        if x < 0:
            is_minus = True
        str_x = ""
        if is_minus:
            str_x = str(x)[1:]
        else:
            str_x = str(x)
        reversed_x = int(str_x[::-1])
        answer = 0
        if is_minus:
            answer = reversed_x * -1
        else:
            answer = reversed_x

        if -2147483648 < answer < 2147483647:
            return answer
        else:
            return 0
