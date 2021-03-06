# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>>  thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки?
# Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?

def thesaurus(*args):
    name_list = {}
    for i in sorted(args):
        letter = i[0]
        if letter in name_list:
            name_list[letter] += [i]
        else:
            name_list[letter] = [i]
    return name_list


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
