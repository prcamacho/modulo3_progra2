from datetime import datetime

def calcular_edad(fecha_nacimiento):
    fecha_actual = datetime.now()
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
    
    if fecha_nacimiento > fecha_actual:
        return -1
    
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def format_title_case(input_string):
    words = input_string.split()
    title_case_words = [word.capitalize() for word in words]
    formatted_string = ' '.join(title_case_words)
    return formatted_string


#EJ9
def quitar_signos(dni1):
    dni="".join(numero for numero in dni1 if numero.isdigit())
    if len(dni) != 8 or dni[0]=='0':
        return 'Error, no valido'
    return int(dni)


#EJ10
def format_name(name):
    return ' '.join([part.capitalize() for part in name.split()])

def validate_dni(dni):
    dni_numeric = ''.join(char for char in dni if char.isdigit())
    
    if len(dni_numeric) != 8:
        return None
    
    return int(dni_numeric)


#EJ13
def convert_binary_to_decimal(binary):
    decimal = 0
    length = len(binary)
    
    for i in range(length):
        if binary[i] == '1':
            exponent = length - 1 - i
            decimal += 2 ** exponent
            
    return decimal


#EJ14
def is_balanced(input_string):
    stack = []
    opening_symbols = '([{'
    closing_symbols = ')]}'
    
    for char in input_string:
        if char in opening_symbols:
            stack.append(char)
        elif char in closing_symbols:
            if not stack:
                return False
            top_symbol = stack.pop()
            if opening_symbols.index(top_symbol) != closing_symbols.index(char):
                return False
    
    return len(stack) == 0    