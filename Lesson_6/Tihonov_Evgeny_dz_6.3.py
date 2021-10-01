from itertools import zip_longest
import json
from pprint import pprint

with open('users.csv', encoding='UTF-8') as users:
    user_list = (users.read().split('\n'))
with open('hobby.csv', encoding='UTF-8') as hobby:
    hobby_list = (hobby.read().split('\n'))

my_dict = dict(zip_longest(user_list, hobby_list))
# Если ключей меньше значений - выходим с кодом 1
for x, h in my_dict.items():
    if x is None:
        exit(1)

with open('dict_for_task_3.csv', 'w', encoding='UTF-8') as f:
    json.dump(my_dict, f, ensure_ascii=False)

pprint(my_dict)
