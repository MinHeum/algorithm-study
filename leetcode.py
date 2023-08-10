# 1061. Lexicographically Smallest Equivalent String to 1061-lexicographically-smallest-equivalent-string
# 파일 제목을 숫자-제목 형식으로 바꾸기

name = input()
name = name.split(' ', 1)

problem_num = name[0]
problem_num = problem_num.split('.')[0]

problem_name = name[1]
problem_name = problem_name.lower()
problem_name = problem_name.replace(' ', '-')

print(problem_num + '-' + problem_name + '.py')
