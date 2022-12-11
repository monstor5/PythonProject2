a = int(input("Степендия = "))
b = int(input("Рассходы = "))
c = b

for i in range(9):
    b = b + b * 0.03
    c += b
v = c - a * 10
print("Сколько денег придется клянчить у родителей =", v)