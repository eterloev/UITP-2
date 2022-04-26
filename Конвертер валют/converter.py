import requests
import xml.etree.ElementTree as ET

def get_rate():
    request = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")

    if request.status_code == requests.codes.ok:    
        xmldoc = ET.fromstring(request.text)
        for node in xmldoc.findall('Valute'):
            if node.find('CharCode').text == "USD":
                return float(node.find('Value').text.replace(',','.'))
    return 73.0

def convertRubToUsd(value, rate):
    return float(int(100*value/rate))/100

def convertUsdToRub(value, rate):
    return float(int(100*value*rate))/100


def printMenu():
    print("""Конвертер валют
1. Конвертировать доллары в рубли
2. Конвертировать рубли в доллары
3. Отобразить курс обмена
4. Вывести инструкции снова
5. Выйти""")


command = '0'
exchangeRate = get_rate()

printMenu()

while command != '5':
    command = input("\n\nВведите номер команды: ")
    
    if command == '1':
        usdvalue = float(input("Введите количество долларов США: "))
        rubvalue = convertUsdToRub(usdvalue, exchangeRate)
        print(str(usdvalue)+" долларов США - " + str(rubvalue) + " рублей")

    elif command == '2':
        rubvalue = float(input("Введите количество рублей: "))
        usdvalue = convertRubToUsd(rubvalue, exchangeRate)
        print(str(rubvalue)+" рублей - " + str(usdvalue) + " долларов США")

    elif command == '3':
        print("Курс: 1 доллар США - "+str(exchangeRate))
    
    elif command == '4':
        printMenu()

    elif command == '5':
        print("Завершение работы...")

    else:
        print('Такой команды не существует')
