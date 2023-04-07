import requests


nazvanie_input = input("Введите название валюты: ")

def get_valute(nazvanie_valuti):
    valuta = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    zapros = valuta.json()    #декодируем json

    inf_curs = zapros['Valute'].get(nazvanie_valuti)
    if inf_curs:
        print(inf_curs['Name'], " ->", inf_curs['Value'], "рублей")
    else:
        print("Валюта", nazvanie_valuti, "не найдена")


get_valute(nazvanie_input.upper())


