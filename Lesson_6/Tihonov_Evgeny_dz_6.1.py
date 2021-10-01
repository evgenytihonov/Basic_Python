from pprint import pprint

result = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as nginx:
    for line in nginx:
        new_line = line.split()
        result.append((new_line[0], new_line[5][1:], new_line[6]))
        print(result)

