import math

# Funções que realizam as operações.

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def subtracao(a, b):
    return a - b

def soma(a, b):
    return a + b

def raiz_quadrada(a):
    return math.sqrt(a)

# Função que valida se a operação digitada é válida.

def validar_operacao():

    operacoes_validas = ['divisao', 'divisão', 'multiplicacao', 'multiplicaçao', 'multiplicação',
                          'subtracao', 'subtraçao', 'subtração', 'soma']
    
    while True:
        try:
            operacao = input('Digite a operação desejada: ').lower()
            if operacao in operacoes_validas:
                print('\nOperação recebida com sucesso.')
                break  
        except ValueError:
            print('Erro.')      

        return operacao  

# Funções que verificam se os números são válidos.

def validar_numero(position: int):
    while True:
        try:
            number = int(input(f'\nDigite o {position} número da operação: '))
            print('\nNúmero recebido com sucesso.')
            return number
        except ValueError:
            print('\nVocê não digitou um número.')
 

# Função que controla o fluxo

def calculadora():

# Armazenamento de valores para condicionais 
 
    divisao1 = ['divisao', 'divisão']
    multiplicacao1 = ['multiplicacao', 'multiplicaçao', 'multiplicação']
    soma1 = ['soma']
    subtracao1 = ['subtracao', 'subtraçao', 'subtração']

# Início do programa
    
    print('\nBem-vindo(a) a calculadora do terminal!\n')
    print('Opções: \n - Divisão \n - Multiplicação \n - Soma \n - Subtração\n - Raíz Quadrada\n' )

# Chamada das funções 
    
    operacao_realizada = validar_operacao()
    n1 = validar_numero(1)
    n2 = validar_numero(2)
        
    
# Validações

    if operacao_realizada in multiplicacao1:
        print(f'\nO resultado da multiplicação entre {n1} e {n2} é {multiplicacao(n1, n2)}.')
    elif operacao_realizada in soma1:
        print(f'\nO resultado da soma entre {n1} e {n2} é {soma(n1, n2)}.')
    elif operacao_realizada in subtracao1:
        print(f'\nO resultado da subtração entre {n1} e {n2} é {subtracao(n1, n2)}.')
    elif operacao_realizada in divisao1:
        print(f'\nO resultado da divisão entre {n1} e {n2} é {divisao(n1, n2)}.')    
    
    print('\nFim do programa.')

if __name__ == '__main__':
    calculadora()