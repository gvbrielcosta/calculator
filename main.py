class Calculator:
    
    
    @classmethod
    def sum(cls, a: float, b: float) -> str:
        return f'da soma é: {a + b}' 
    
    @classmethod
    def sub(cls, a: float, b: float) -> float:
        return f'da subtração é: {a - b}' 
    
    @classmethod
    def div(cls, a: float, b: float) -> float:
        return f'da divisão é: {a / b}' 
    
    @classmethod
    def mult(cls, a: float, b: float) -> float:
        return f'da multiplicação é: {a * b}' 
    
def get_operation():
    
    valid_operations = {

        'soma': Calculator.sum,
        'subtraçao': Calculator.sub,
        'multiplicacao': Calculator.mult,
        'divisao': Calculator.div,
        'divisão': Calculator.div,
        'multiplicação': Calculator.mult,
        'subtração': Calculator.sub

    }
    print('\n - Soma \n - Multiplicação \n - Divisão \n - Subtração')
    
    while True:
        try:
            str_operation = input('Digite a operação desejada: ')
            return valid_operations[str_operation]
        
        except KeyError:
           print('Você não digitou uma operação válida.')


def get_number(position: str) -> float:
    while True:
        try:
            num = float(input(f'Digite o {position} número da operação: '))
            return num
        except ValueError:
            print('Você não digitou um número.')
   
def start():

    print("Bem vindo a calculadora")
    operation = get_operation()
    number_1 = get_number('primeiro')
    number_2 = get_number('segundo')
    print(f'O resultado {operation(number_1, number_2)}')


start()
