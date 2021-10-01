from collections import Counter

result = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as nginx:
    for line in nginx:
        new_line = line.split()
        result.append((new_line[0], new_line[5][1:], new_line[6]))

ip_adresess = [x[0] for x in result]
spammer_ip = Counter(ip_adresess).most_common()[0]
print(f'spamer = {spammer_ip}')

