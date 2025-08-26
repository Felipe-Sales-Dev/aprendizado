#Primeiro projeto de calculadora simples
#Autor: Felipe
#Função: fazer contas de adição, subtração, multiplicação, divisão
###########################################################################################
#First simple calculator project
#Author: Felipe
#Function: Solve simple math problems with Addition, Subtraction, Multiplication, Division
############################################################################################

print ("--------- Calculadora v1.0 ---------")

sair = False
while sair == False:

    num1 = input ("Digite o primeiro número: ")
    num1 = int(num1)
    #usamos a função int para transformar a string em numero inteiro
    #using the function int to transform the string in flat number
    operador = input("digite o operador (+,-,/,*): ")
    num2 = input("digite o segundo número: ")
    num2 = int(num2)

    #soma / addition
    if operador == "+":
        operacao = num1 + num2
    #subtração / subtraction
    if operador == "-":
        operacao = num1 - num2
    #multiplicação / multiplication
    if operador == "*":
        operacao = num1 * num2
    #divisão / division
    if operador == "/":
        operacao = num1 / num2
        
    print("Resultado :")
    print(operacao)

    saida = input("deseja sair da calculadora? (s/n)")
    if saida == "s":
        sair = True
        print("ate mais")