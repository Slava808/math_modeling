print('Напиши год')
year = int(input())

if year % 4 == 0 and year % 100 or year % 400:
    print('Год високосный')
else:
    print('Год невисокосный')
