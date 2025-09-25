bio = input('ФИО:')
fio = bio.split()
initials = ''.join([i[0] for i in fio]).upper()
dlina = 0
for l in bio:
    dlina += 1
    if l == ' ':
        dlina -= 1
print(f'Инициалы:{initials}.')
print(f'Длина (символов):{dlina}')