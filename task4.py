# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

s = int(input('Количество журавликов: '))
if s % 6 != 0:
    print('Введите число кротное шести')
else:
    petya = int(s/6)
    serg = int(petya)
    katya = int(4*petya)
    print(petya, katya, serg)