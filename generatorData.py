import sys, random, time
import mysql.connector

mydb = mysql.connector.connect(
  host="107.20.30.117",
  user="lucas",
  password="urubu100",
  database="generator"
)

mycursor = mydb.cursor()

def insert(values):
  sql = "INSERT INTO algas (cidade, produto, pagamento, dia, mes, quantidade, valor, total, tempo, memoria) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

  mycursor.execute(sql, values)

  mydb.commit()

cidades = ['Sao Paulo', 'Rio de Janeiro', 'Salvador', 'Curitiba', 'Alagoas', 'Natal', 'Angra dos Reis']
produtos = ['Frango', 'Sorvete', 'Feijao', 'Whisky', 'Arroz', 'Doritos', 'Ruffles', 'Chocolate']
valores = [10.99, 16.85, 6.80, 89.99, 7.8, 7.9, 5.67, 8.5]
pagamento = ['Debito', 'Credito', 'Dinheiro']
semana = ['Domingo', 'Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
meses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def transaction(range):
    tempo_inicial = (time.time())
    lista = []
    for item in range:
        cidade = cidades[random.randrange(0, (len(cidades)), 1)]
        posicaoProdutoValor = random.randrange(0, (len(produtos)), 1)
        produto = produtos[posicaoProdutoValor]
        valor = valores[posicaoProdutoValor]
        formaPagamento = pagamento[random.randrange(0, (len(pagamento)), 1)]
        dia = semana[random.randrange(0, (len(semana)), 1)]
        mes = meses[random.randrange(0, (len(semana)), 1)]
        quantidade = random.randint(1, 1000)
        totalCompra = (quantidade * valor)
        tempo_append = (time.time())
        tempo_final = (tempo_append - tempo_inicial)
        lista.append(item)
        tamanho = sys.getsizeof(lista)
        values = (cidade, produto, formaPagamento, dia, mes, quantidade, valor, totalCompra, tempo_final, tamanho)
        print(values)
        insert(values)

print('*_* Menu *_*')
print('Inserir')
print('Sair')
 
while True:
    do = input('O que voce deseja fazer?').split()
    
    operation = do[0]
    if operation == 'Inserir':
      valorInicial = input('Digite o valor inicial: ')
      valorFinal = input('Digite o valor final: ')
      intervalo = input('Digite o intervalo: ')
      transaction(range(int(valorInicial), int(valorFinal), int(intervalo)))

    elif operation == 'Sair':
        print('Valeu tmj, primo')
        break