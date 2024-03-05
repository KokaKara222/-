import csv


with open('FIOandTelephone.csv', "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, ["FIO", 'Telephone'])
    f = input('Введите ФИО человека: ')
    for i in reader:
        if f== i['FIO']:
            print('Номер телефона: ', i['Telephone'])
            break
    else:
        print('Не найден')
