import sys, random, time
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="39813385",
  database="generator"
)

mycursor = mydb.cursor()

def insert(values):
  sql = "INSERT INTO algas (cidade, produto, pagamento, dia, valor, tempo, memoria) VALUES (%s, %s, %s, %s, %s, %s, %s)"

  mycursor.execute(sql, values)

  mydb.commit()
  print(mycursor.rowcount, "record inserted.")

cidades = ['Sao Paulo', 'Rio de Janeiro', 'Florianopolis', 'Curitiba', 'Alagoas', 'Natal']
produtos = ['Batata', 'Acucar', 'Feijao', 'CocaCola', 'Arroz']
pagamento = ['Dinheiro', 'Debito', 'Credito']
semana = ['Domingo', 'Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado']

def transaction(range):
    tempo_inicial = (time.time())
    lista = []
    for item in range:
        cidade = cidades[random.randrange(0, (len(cidades)-1), 1)]
        produto = produtos[random.randrange(0, (len(produtos)-1), 1)]
        formaPagamento = pagamento[random.randrange(0, (len(pagamento)-1), 1)]
        dia = semana[random.randrange(0, (len(semana)-1), 1)]
        quantidade = random.randint(1, 1000)
        tempo_append = (time.time())
        tempo_final = (tempo_append - tempo_inicial)
        lista.append(item)
        tamanho = sys.getsizeof(lista)
        values = (cidade, produto, formaPagamento, dia, quantidade, tempo_final, tamanho)
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