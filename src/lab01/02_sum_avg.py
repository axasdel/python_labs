a = float(input("a:").replace(',', '.'))
b = float(input("b:").replace(',', '.'))
summa = a + b
avg = str((summa / 2))
if int(avg[3]) >= 5: avg = str(float(avg) + 0.01)
print(f'sum={summa}, avg ={avg[:4]}')