import re


n, m = map(int, input().split())


matrix = [input() for _ in range(n)]


decoded_string = "".join(["".join(column) for column in zip(*matrix)])


pattern = r'(?<=\w)[^\w]+(?=\w)'


result = re.sub(pattern, ' ', decoded_string)

print(result)
