import requests
import json

URL = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'


def get_information(url):
    response = requests.get(url)
    assert response.status_code == 200, f'Algo salió mal: {response.status_code}'
    content = json.loads(response.content)
    return content


def run():
    pesos_to_dolars = lambda pesos, dolar_value: pesos / dolar_value
    dolars_to_pesos = lambda dolars, dolar_value: dolars * dolar_value

    info = get_information(URL)
    dolar_value = float(info[0]['casa']['compra'].replace(',', '.'))

    choice = input('¿Qué operación quieres hacer? \n 1: Dolar a pesos \n 2: Pesos a dólares \n Elige: ')
    if choice == '1':
        dolars = float(input('¿Cuántos dólares tienes? '))
        pesos = round(dolars_to_pesos(dolars, dolar_value), 2)
        print(f'Equivalen a {pesos} pesos.')
    elif choice == '2':
        pesos = float(input('¿Cuántos pesos tienes? '))
        dolars = round(pesos_to_dolars(pesos, dolar_value), 2)
        print(f'Equivalen a {dolars} dólares.')
    else: 
        print('Escribe una opción correcta')


if __name__ == '__main__':
    run()
