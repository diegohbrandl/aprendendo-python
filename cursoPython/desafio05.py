#Faça um programa que leia um numero inteiro e mostre na tela seu antecessor e seu sucessor

valor = int(input('Digite o valor! '))
print(' O valor é >> {}\n O antecessor é >> {}\n e o sucessor é >> {}'.format(valor, valor - 1, valor + 1 ))

#Faça um programa que um numero e mostre seu dobro, triplo e a raiz quadrada

valor = int(input('Digite o valor! '))
print(' Valor >> {}\n Dobro >> {}\n Triplo >> {}\n Raiz Quadrada >> {:.3f}'.format(valor, valor * 2, valor * 3, valor **(1/2)))

#Desenvolva um programa que leia as duas notas de um aluno e mostre a sua media

nota1 = float(input('Nota 1 >> '))
nota2 = float(input('Nota 2 >>'))
media = (nota1 + nota2) / 2
print(' Nota 1 >> {}\n Nota 2 >> {}\n Media >> {:.2f}'.format(nota1, nota2, media))

# Escreva um programa que receba um valor em metros e o exiba convertendo em centrimetros e milimitros

valorMetro = float(input('Quantos metros? '))
print('O valor do metro é >> {}\nConvertido para centimetro >> {:.2f}\nConvertido para milimetro >> {:.2f}'.format(valorMetro, valorMetro * 100, valorMetro * 1000))

#Faça um programa que leia um numero inteiro e mostre a sua tabuada na tela

valor = int(input('Digite o valor '))
for i in range(11):
    total = valor * i
    print('{} x {} = {} '.format(valor, i, total))
    i + 1

#Crie um programa que leia quanto dinheiro uma  pessoa tem em real e mostre quantos dolares ela pode comprar
#Cotação do dolar no dia do codigo $ 5,79

dinheiro = float(input('Quantos dinheiro você tem? R$ '))
dolar = dinheiro / 5.79
print('Com esse valor R${} você consegue comprar ${:.2f} dolares '.format(dinheiro, dolar))

#Faça um programa que leia a largura e a altura de um parede em metros, calcule a sua area e a quantidade de tinta >>
# >> nescessaria para pinta-la sabendo que cada litro da tinta pinta uma area de 2m²

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
areaTotal = altura * largura
totalTinta = areaTotal / 2
print('altura > {}\n largura > {}\n total {}m²'.format(altura, largura, areaTotal))
print(' O total nescessario de tinta para pintar a area é > {} latas de tinta'.format(totalTinta))


#Faça um programa que leia o preço de um produto e mostre o seu novo preço com 5% de desconto

valorProduto = float(input('Qual o valor do produto? '))
valorDesconto = valorProduto - ((valorProduto * 5 ) / 100)
print('O valor do produto com desconto é : {}'.format(valorDesconto))


#Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

salario = float(input('Salario >>'))
novoSalario = salario + ((salario * 15)/ 100)
print('Seu novo salario >> {}'.format(novoSalario))
