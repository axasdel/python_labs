**ЛАБОРАТОРНАЯ РАБОТА 1**

*Задание 1. Блок А*
```python
name  = input('Имя:')
age = int(input('Возраст:'))
new_age = age + 1
print(f'Привет, {name}! Через год тебе будет {new_age}')
```
![img01](https://github.com/axasdel/python_labs/blob/main/src/images/img01.png)

*Задание 2. Блок А*
```python
a = float(input("a:").replace(',', '.'))
b = float(input("b:").replace(',', '.'))
summa = a + b
avg = str((summa / 2))
if int(avg[3]) >= 5: avg = str(float(avg) + 0.01)
print(f'sum={summa}, avg ={avg[:4]}')
```
![img02](https://github.com/axasdel/python_labs/blob/main/src/images/img02.png)

*Задание 3. Блок А*
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

*Задание 4. Блок А*
```python
min = int(input('Минуты:'))
hours = min // 60
minut = min % 60
print(f'{hours}:{minut}')
```
![img04](https://github.com/axasdel/python_labs/blob/main/src/images/img04.png)

*Задание 5. Блок А*
```python
bio = input('ФИО:')
fio = bio.split()
initials = ''.join([i[0] for i in fio]).upper()
dlina = 0
for l in fio:
    dlina += len(l)
print(f'Инициалы:{initials}.')
print(f'Длина (символов):{dlina + 2}')
```
![img05](https://github.com/axasdel/python_labs/blob/main/src/images/img05.png)



**ЛАБОРАТОРНАЯ РАБОТА 2**

*Задание 1. Блок А*
```python
nums = [1, 3, 2, 3]
def min_max(nums):
    nums_tup = []
    if len(nums) > 0:
        mini = nums_tup.append(min(nums))
        maxi = nums_tup.append(max(nums))
        print(tuple(nums_tup))
    else:
        raise ValueError
min_max(nums)
```
![img01](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img01.png)
![img11](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img11.png)
![img12](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img12.png)

*Задание 2. Блок А*
```python
nums = []
def unique_sorted(nums):
    new_nums = sorted(set(nums))
    print(new_nums)
unique_sorted(nums)
```
![img02](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img02.png)
![img21](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img21.png)
![img22](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img22.png)

*Задание 3. Блок А*
```python
mat = [[1, 2], [3, 4]]
def flatten(mat):
    new_mat = []
    for num in mat:
        if type(num) == tuple or type(num) == list:
            for i in range(len(num)):
                if num[i] != '':
                    new_mat.append(num[i])
        else:
            raise ValueError
    print(new_mat)
flatten(mat)
```
![img03](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img03.png)
![img31](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img31.png)
![img32](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/img32.png)

*Задание 1. Блок Б*
```python
mat= [[1, 2], [3, 4]]

def check_rvanost(mat):
    dlina = len(mat[-1])
    for x in mat:
        if len(x) != dlina:
            raise ValueError
        else:
            return True
def transpose(mat):
    if check_rvanost:
        new_mat = []
        for stolbec in range(len(mat[-1])):
            new_row = []
            for row in range(len(mat)):
                new_row.append(mat[row][stolbec])
            new_mat.append(new_row)
    print(new_mat)
transpose(mat)
```
![matrix1](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/matrix1.png)

*Задание 2. Блок Б*
```python
mat = [[1, 2], [3]]
def check_rvanost(mat):
    for i in range(len(mat)):
        if len(mat[i]) == len(mat[i+1]):
            return True
        else:
            return False
def row_sums(mat):
    new_mat = []
    for x in mat:
        if type(x) == list and check_rvanost(mat):
            summa = 0
            for i in range(len(x)):
                summa += x[i]
            new_mat.append(summa)
        else:
            raise ValueError
    print(new_mat)
row_sums(mat)
```
![matrix2](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/matrix2.png)

*Задание 3. Блок Б*
```pyhon
```
![matrix3](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/matrix3.png)

*Задание 1. Блок С*
```python
mat = [[1, 2], [3]]
def check_rvanost(mat):
    for i in range(len(mat)):
        if len(mat[i]) == len(mat[i+1]):
            return True
        else:
            return False
def row_sums(mat):
    new_mat = []
    for x in mat:
        if type(x) == list and check_rvanost(mat):
            summa = 0
            for i in range(len(x)):
                summa += x[i]
            new_mat.append(summa)
        else:
            raise ValueError
    print(new_mat)
row_sums(mat)
```
![tuples](https://github.com/axasdel/python_labs/blob/main/src/images/lab02/tuples.png)