"""
METODO DE ORDENAÇÃO DE DADOS - QUICKSORT
"""

def particionar(lista,esquerda,direita):
    pivo = lista[direita] #o pivo é o ultimo elemento
    menores = esquerda #o elemento que são menores que o pivo ficam na esquerda
    for i in range(esquerda,direita): #a variavel i vai percorrer toda a lista, para fazer comparação
        if lista[i] <= pivo: #se o numero na posição i, for menor ou igual ao pivo
            lista[menores],lista[i] = lista[i],lista[menores] #realiza a troca de posição
            menores += 1 #incrementa mais um na variavel menores, já que têm mais numero menor que o pivo
    lista[menores], lista[direita] = pivo, lista[menores] #apos percorrer toda a lista, realiza a ultima troca (o pivo)
    return menores #retorna a posição do pivo


def quicksort(lista, esquerda=0, direita=None):
    if direita is None: #caso não for especificada, determina a posição da extrema direita
      direita = len(lista)-1
    if esquerda < direita: #se a lista for vazia, não realiza a ordenação
        p = particionar(lista, esquerda, direita) #vai dividir a lista em duas, lista menores que o pivo e lista maiores que o pivo
        quicksort(lista, esquerda, p-1) #realizar o ordenamento da lista da esquerda (os menores que o pivo)
        quicksort(lista, p+1, direita) #realizar o ordenamento da lista da direita (os maiores que o pivo)