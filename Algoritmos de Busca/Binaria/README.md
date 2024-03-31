# Busca binária

> O que é ?

É uma forma eficiente de procurar um elemento em uma lista ( Array ) de elementos, onde ela vai ser mais performática do que a forma de busca de ir pulando de um em um nas posições de um array

Vamos supor que você queira encontar um usuário com um ID em um banco de dados onde tem mais de mais de 10.000 usuarios, cá entre nós que usando a forma de ir item por item iria demorar muito. Então eu irei explicar para você como funciona

> Como funciona:

- Primeiramente devemos saber que nesse algoritmo ele precisa que a lista esteja ordenada, para os nossos exemplos vamos usar Python mas você pode usar com qualquer outra

```py
# Nossa lista ( array ) bagunçado
numeros = [2, 3, 1, 4, 8, 6, 71, 10, 5, 9]

# Agora criamos uma função para executar essa busca binaria
# vamos fazer da forma mais simples possivel você pode alterar da forma que quiser

def busca_binaria():
    # Aqui ele vai pedir um número para o usuário
    number = int(input("Digite o número você quer: "))
    
    # Aqui ele vai arrumar nosso array de forma crescente 
    numeros.sort()
```
 
> Lógica:

Vamos supor que uma pessoa jogue um jogo de advinhação com você, ela diz: "Eu vou escolher um número entre 1 a 100, e você tem que adivinhar esse número se for muito maior que meu número eu direi ALTO e se for menor que meu número eu vou dizer BAIXO"

Uma forma de adivinhar é ir chutando número por número do 1 ao 100, so que a forma mais eficiente é você falar a metade. Como assim ? Imaginamos que essa pessoa escolheu o numero 60, se fosse da primeira forma tu teria que chutar 60 vezes ate achar o numero, mas chutando o número 50 que é metade de 100, a pessoa vai dizer ALTO e ai você simplesmente descartou 50 números em um único chute e assim vai continuando do 50 pra frente a proxima metade seia 75 porque você dividiu a metade de 100 (50) pela metade de novo ai você vai diminuindo pela metade ate chegar ao valor certo, deu para sacar?

Então no código eu vou precisar do valor minimo ( que é o valor inicial ) e o valor maximo ( que seria o maior valor ) e depois descobrir o meio


Pessoa 1: "Ah mais Erick e se a pessoa que eu to procurando for a primeira nem vai fazer sentido eu usar essa tal busca binária"

Eu: "Claro, mas e se por um acaso a pessoa que você procura seja a última ?  A sua teória cai por terra pois de é mais fácil usar esse algoritmo do que ter que lidar depois com performance "