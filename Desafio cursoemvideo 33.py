abc = int(input('Digite um ano qualquer: '))
if abc%4==0 and abc%100!=0 or abc%400==0:
    print('O ano escolhido é bissexto!')
else:
    print('O ano escolhido não é bissexto')

'''year = int(input("Enter a year: "))

if year > 1582:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('Leap year')
    else:
        print('Commom year')
else:
    print('Not within the Gregorian calendar period')
    '''