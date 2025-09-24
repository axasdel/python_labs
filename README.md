**ЛАБОРАТОРНАЯ РАБОТА 1**

*Задание 1*
```python
name  = input('Имя:')
age = int(input('Возраст:'))
new_age = age + 1
print(f'Привет, {name}! Через год тебе будет {new_age}')
```
![img01](https://github.com/axasdel/python_labs/blob/main/src/images/img01.png)

*Задание 2*
```python
a = float(input("a:").replace(',', '.'))
b = float(input("b:").replace(',', '.'))
summa = a + b
avg = str((summa / 2))
if int(avg[3]) >= 5: avg = str(float(avg) + 0.01)
print(f'sum={summa}, avg ={avg[:4]}')
```
![img02](https://github.com/axasdel/python_labs/blob/main/src/images/img02.png)

*Задание 3*
```python
price = float(input('price:'))
discount = float(input('discount:'))
vat = float(input('vat:'))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки:{base}')
print(f'НДС:{vat_amount}')
print(f'Итого к оплате:{total}')
```
![img03](https://github.com/axasdel/python_labs/blob/main/src/images/img03.png)

*Задание 4*
```python
min = int(input('Минуты:'))
hours = min // 60
minut = min % 60
print(f'{hours}:{minut}')
```
![img04](https://github.com/axasdel/python_labs/blob/main/src/images/img04.png)

*Задание 5*
```python
bio = input('ФИО:')
fio = bio.split()
initials = ''.join([i[0] for i in fio]).upper()
dlina = 0
for l in bio:
    dlina += 1
print(f'Инициалы:{initials}.')
print(f'Длина (символов):{dlina}')
```
![img05](https://github.com/axasdel/python_labs/blob/main/src/images/img05.png)
