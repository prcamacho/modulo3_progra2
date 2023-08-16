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


