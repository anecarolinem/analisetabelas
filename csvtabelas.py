import csv

with open('clientes.csv', 'r') as arquivo:
    dados = csv.reader(arquivo) #abrir arquivo

    for dado in dados:#interar e a abrir para leitura
        print(dado)

with open('clientes.csv', 'r') as arquivo:
    dados = csv.DictReader(arquivo) #abrir arquivo em forma de dicionario

    for dado in dados:#interar e a abrir para leitura
      print(dado)
with open('../clientes.csv', 'r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)] #abrir arquivo em forma de dicionario


with open('../clientes2.csv', 'w') as arquivo: #criar novo arquivo com novas regras
    escreve = csv.writer( #regras ´para a nova inscrita
        arquivo,
        delimiter= ',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3],
        ]
    )
    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
