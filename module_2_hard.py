import random


def parol():
    list_parol = []
    zamok = 0
    range_zamok = range(3, 21)
    chislo_zamok = random.choice(range_zamok)
    zamok = zamok + chislo_zamok
    range_parol = range(1, 21)
    for i in range_parol:
        range_parol_2 = range(i + 1, 21)
        for j in range_parol_2:
            if i != zamok and j != zamok and zamok % (i + j) == 0:
                list_parol.append(i)
                list_parol.append(j)
    print(f'{zamok} - число из первой вставки')
    print(*list_parol, '- нужный пороль')


parol()

for _ in range(5):
    print(f'Будь проклето это задание')
