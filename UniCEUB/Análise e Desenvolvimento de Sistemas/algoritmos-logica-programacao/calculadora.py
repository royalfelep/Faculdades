import sys

######## Variáveis #########
memoria = None

######### Funcoes ##########

#Função Memória
def menuMemoria(resultado):
    global memoria
    opOpcao = None
    while opOpcao != "0":
        # Menu visual
        print("----------------------------------------------------------------------------")
        print("| 1: MS | 2: M(+) | 3: M(-) | 4: M(*) | 5:M(/) | 6: MC | 0: Voltar ao Menu |")
        print("----------------------------------------------------------------------------\n")
        # Direcionando as operações
        opOpcao = input("Digite o número da opção desejada: ")
        # Função MS
        if opOpcao == "1":
            if resultado == memoria:
                print("\nNúmero já está guardado na memória.\n")
            else:
                memoria = resultado
                print("\nNúmero guardado na memória.\n")
        # Função M(+)
        elif opOpcao == "2":
            if memoria == None:
                print("\nNão há nenhum número guardado na memória.\n")
            else:
                resultado += memoria
                print("\nResultado: {}\n".format(resultado))
        # Função M(-)
        elif opOpcao == "3":
            if memoria == None:
                print("\nNão há nenhum número guardado na memória.\n")
            else:
                resultado -= memoria
                print("\nResultado: {}\n".format(resultado))
        # Função M(*)
        elif opOpcao == "4":
            if memoria == None:
                print("\nNão há nenhum número guardado na memória.\n")
            else:
                resultado *= memoria
                print("\nResultado: {}\n".format(resultado))
        #Função M(/)
        elif opOpcao == "5":
            if memoria == None:
                print("\nNão há nenhum número guardado na memória.\n")
            else:
                resultado /= memoria
                print("\nResultado: {}\n".format(resultado))
        # Função MC
        elif opOpcao == "6":
            memoria = None
            print("\nMemória limpa.\n")
        # Break
        elif opOpcao == "0":
            break
        # Caso não caia em nenhum IF, printa Operação inválida.
        else:
            print("Operação inválida.\n")

#Função Somar
def somar():
    global memoria
    def innerSomar():
        qntNumeros = None
        # Input: Quantos números seráo somados + validação
        try:
            qntNumeros = int(input("\nQuantos números deseja somar? "))
        except:
            print("\nNúmero Inválido.")
            try:
                qntNumeros = int(input("\nQuantos números deseja somar? "))
            except:
                return print("\nNúmero Inválido. Voltando ao Menu.\n")
        numero = 0
        # Input: Primeiro número da soma + validação
        try:
            numero = float(input("\nDigite um número: "))
        except:
            print("\nNúmero Inválido.\n")
            try:
                numero = float(input("Digite outro número: "))
            except:
                return print("\nNúmero Inválido. Voltando ao Menu.\n")
        # Input: resto dos número da soma + validação
        i=1
        while i < qntNumeros:
            try:
                numero += float(input("\nDigite o próximo número: "))
            except:
                print("\nNúmero Inválido.\n")
                try:
                    numero += float(input("Número Inválido. Digite novamente o número: "))
                except:
                    return print("\nOperação inválida. Voltando ao Menu.\n")
            i +=1
        return numero
    # Chamada da função com resultado da soma + validação
    resultado = innerSomar()
    if resultado == None:
        return
    print("\nResultado: {}\n".format(resultado))
    # Chamada da função que exibe o menu de memória
    menuMemoria(resultado)
    return print("\nSaindo da função Somar.\n")

#Função Subtrair
def subtrair():
    global memoria
    def innerSubtrair():
        qntNumeros = None
        # Input: Quantos números seráo subtraidos + validação
        try:
            qntNumeros = int(input("\nQuantos números deseja subtrair? "))
        except:
            print("\nNúmero Inválido.")
            try:
                qntNumeros = int(input("\nQuantos números deseja subtrair? "))
            except:
                return print("\nNúmero Inválido. Voltando ao Menu.\n")
        numero = 0
        # Input: Primeiro número da subtração + validação
        try:
            numero = float(input("\nDigite um número: "))
        except:
            print("\nNúmero Inválido.\n")
            try:
                numero = float(input("Digite outro número: "))
            except:
                return print("\nNúmero Inválido. Voltando ao Menu.\n")
        # Input: Resto dos números da subtração + validação
        i=1
        while i < qntNumeros:
            try:
                numero -= float(input("\nDigite o próximo número: "))
            except:
                print("\nNúmero Inválido.\n")
                try:
                    numero -= float(input("Número Inválido. Digite novamente o número: "))
                except:
                    return print("\nOperação inválida. Voltando ao Menu.\n") 
            i +=1
        return numero
    # Chamada da função com resultado da subtração + validação
    resultado = innerSubtrair()
    if resultado == None:
        return
    print("\nResultado: {}\n".format(resultado))
    # Chamada da função que exibe o menu da memória
    menuMemoria(resultado)
    return print("\nSaindo da função Subtrair.\n")

#Função Multiplicar
def multiplicar():
    global memoria
    def innerMultiplicar():
        qntNumeros = None
        # Input: Quantos números serão multiplicados + validação
        try:
            qntNumeros = int(input("\nQuantos números deseja multiplicar? "))
        except:
            print("\nNúmero Inválido.")
            try:
                qntNumeros = int(input("\nQuantos números deseja multiplicar? "))
            except:
                return print("\nNúmero Inválido. Voltando ao Menu.\n")
        numero = 0
        # Input: Primeiro número da multiplicação + validação
        try:
            numero = float(input("\nDigite um número: "))
        except:
            print("\nNúmero Inválido.\n")
            try:
                numero = float(input("Digite outro número: "))
            except:
                return print("\nNúmero Inválido. Voltando ao Menu.\n")
        # Input: Resto dos números da multiplicação + validação
        i=1
        while i < qntNumeros:
            try:
                numero *= float(input("\nDigite o próximo número: "))
            except:
                print("\nNúmero Inválido.\n")
                try:
                    numero *= float(input("Número Inválido. Digite novamente o número: "))
                except:
                    return print("\nOperação inválida. Voltando ao Menu.\n") 
            i +=1
        return numero
    # Chamada da função com resultado da multiplicação + validação
    resultado = innerMultiplicar()
    if resultado == None:
        return
    print("\nResultado: {}\n".format(resultado))
    # Chamada da função que exibe o menu da memória
    menuMemoria(resultado)
    return print("\nSaindo da função Multiplicar.\n")

#Função Dividir
def dividir():
    global memoria
    def innerDividir():
        qntNumeros = None
        # Input: Quantos números serão divididos + validação
        try:
            qntNumeros = int(input("\nQuantos números deseja dividir? "))
        except:
            print("\nNúmero Inválido.")
            try:
                qntNumeros = int(input("\nQuantos números deseja dividir? "))
            except:
                return print("\nNúmero Inválido. Voltando ao Menu.\n")
        numero = 0
        # Input: Primeiro número da divisão + validação
        try:
            numero = float(input("\nDigite um número: "))
        except:
            print("\nNúmero Inválido.\n")
            try:
                numero = float(input("Digite outro número: "))
            except:
                return print("\nNúmero Inválido. Voltando ao Menu.\n")
        # Input: Resto dos números da divisão + validação
        i=1
        while i < qntNumeros:
            try:
                numero /= float(input("\nDigite o próximo número: "))
            except:
                print("\nNúmero Inválido.\n")
                try:
                    numero /= float(input("Número Inválido. Digite novamente o número: "))
                except:
                    return print("\nOperação inválida. Voltando ao Menu.\n") 
            i +=1
        return numero
    # Chamada da função com resultado da divisão + validação
    resultado = innerDividir()
    if resultado == None:
        return
    print("\nResultado: {}\n".format(resultado))
    # Chamada da função que exibe o menu da memória
    menuMemoria(resultado)
    return print("\nSaindo da função Dividir.\n")

######### Console ##########
# Dicionário usado para se referir às funções
operacoes = {
    "1": somar,
    "2": subtrair,
    "3": multiplicar,
    "4": dividir
}

# Menu principal
opcao = None
while opcao != 0:
    print("-------------------------------------------------------------------------------")
    print("| 1: Somar | 2: Subtrair | 3: Multiplicar| 4: Dividir | 0: Fechar Calculadora |")
    print("-------------------------------------------------------------------------------")
    opcao = input("\nDigite o numero da opcao desejada: ")
    try:
        if(opcao == "0"):
            print("\nVocê fechou a calculadora.\n")
            break
        else:
            # Executa as funções a partir do dicionário
            operacoes[opcao]()
    except:
        print("\nOpção inválida.\n")