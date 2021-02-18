import sys

'''
만 나이: 국제적인 표준 방법이다. 한국에서도 법에서는 만 나이만을 사용한다.
세는 나이: 한국에서 보통 나이를 물어보면 세는 나이를 의미한다.
연 나이: 법률에서 일괄적으로 사람을 구분하기 위해서 사용하는 나이이다.
'''

b_year, b_month, b_day = map(int, sys.stdin.readline().split())
q_year, q_month, q_day = map(int, sys.stdin.readline().split())

b_mmdd = b_month * 100 + b_day
q_mmdd = q_month * 100 + q_day

happybirthday = 0
if b_mmdd > q_mmdd:
    happybirthday = 1


# 만 나이
print(q_year - b_year - happybirthday)

# 세는 나이: b_year 과 q_year 만 있으면 구할 수 있다.
print(q_year - b_year + 1)

# 연 나이 : b_year 과 q_year 만 있으면 구할 수 있다.
print(q_year - b_year)
