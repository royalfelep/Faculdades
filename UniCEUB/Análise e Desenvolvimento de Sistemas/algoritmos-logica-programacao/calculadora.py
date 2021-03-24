######## Variáveis #########
memoria = None

######### Funcoes ##########
def soma():
    global memoria

    def innerSoma():
        qntNumeros = int(input("\nQuantos numeros deseja somar? "))
        i=0
        numero = 0
        while i < qntNumeros:
            numero += int(input("Digite um numero: "))
            if isinstance(numero,int) == False:
                print("Numero Inválido.")
                break
            else:
                i +=1
        return numero

    resultado = innerSoma()
    print("\nSoma = {}\n".format(resultado))

    somaOpcao = None
    while somaOpcao != "2":
        print("---------------------------------------")
        print("1: Guardar número na memória | 2: Sair") # Menu funcao soma
        print("---------------------------------------\n")
        somaOpcao = input("Digite o numero da opcao desejada: ")
        if somaOpcao == "1":
            if resultado == memoria:
                print("\nNúmero já está guardado na memória\n")
            else:
                memoria = resultado
                print("Número guardado na memória.\n")
        elif somaOpcao == "2":
            break
        else:
            print("Operacao invalida\n")
            
    return print("\nSaindo da função soma\n")


######### Console ##########
operacoes = {
    "1": soma,
}

opcao = None
while opcao != "0":
    print("---------------------------------------")
    print(" 1: Somar | 2: Subtrair | 0: Sair")
    print("---------------------------------------")
    opcao = input("Digite o numero da opcao desejada: ")

    if opcao == "1":
        operacoes[opcao]()
