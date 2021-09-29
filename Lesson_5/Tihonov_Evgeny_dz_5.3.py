tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def tutor_gen(*iterables):
    tutors, klasses = iterables
    for idx, name in enumerate(tutors):
        yield name, klasses[idx] if idx < len(klasses) else None


test_generator = tutor_gen(tutors, klasses)
# check output
print(type(test_generator))
for tpl in test_generator:
    print(tpl)

print('=' * 20)
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В']
test_generator_2 = tutor_gen(tutors, klasses)
for tpl in test_generator_2:
    print(tpl)