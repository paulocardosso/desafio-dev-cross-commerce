import requests

def extrair():
    #listcompleta = [10,20,15,30,13] #so para teste
    listcompleta = []  #uma lista vazia para armazenar os numeros coletados da API
    c = 1  #um contador para percorrer as paginas existentes
    while True:
        response = requests.get(
            'http://challenge.dienekes.com.br/api/numbers?page={}'.format(c))  #captura os numeros da pagina
        if (response.status_code == 200):  # verifica se o processo anterior foi OK, para continuar com o processo de extração
            if ((response.json()['numbers'] == []) or (
                response.json()['numbers'] == None)):  # verifica se o elemento é nulo ou vazio
                break  # se for, significa que acabou o numero de paginas, logo o while é finalizado
            else:  # senao, se existir elemento, faça a operação de extração
                for num in response.json()['numbers']:  # um for para percorrer a lista obtida
                    listcompleta.append(num)  # cada item da lista é add na listacompleta criada no inicio desse metodo
            c += 1  # pula para a proxima pagina, caso o status seja 200 (OK), senão tenta novamente capturar os numeros da pagina
    return listcompleta #retorna a listacompleta com todos os numeros da api