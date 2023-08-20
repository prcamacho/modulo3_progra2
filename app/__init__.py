from flask import Flask, request, jsonify, render_template
from config import Config
from datetime import datetime
import json

from .utils.utilstp3 import calcular_edad, format_title_case, quitar_signos, format_name, validate_dni, convert_binary_to_decimal, is_balanced

def init_app():
    """Crea y configura la aplicación Flask"""

    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)

    app.config.from_object(Config)
    
    
    # EJ1
    @app.route('/')
    def bienvenido():
        return ({'message': f'Bienvenido'},200,{'Content-Type': 'application/json'})
    
    
    #EJ2
    @app.route('/info')
    def bienvenido_appname():
        return ({'message': f'Bienvenido a {Config.APP_NAME}'},200,{'Content-Type': 'application/json'})
    
    
    #EJ3
    @app.route('/about')
    def about():
        about ={
            "app_name": Config.APP_NAME,
            "description": "App para flask",
            "developers": [
                {
                    "nombre":"fido",
                    "apellido":"tito"
                },
                                {
                    "nombre":"firulais",
                    "apellido":"chico"
                }
                
            ],
            "version": "1.0.0"
        }
        return (about,200,{'Content-Type': 'application/json'})
    
    
    #EJ4
    @app.route('/sum/<int:num1>/<int:num2>')
    def sum_path(num1, num2):
        response ={
            "sum": num1 + num2
        }

        return (response,200,{'Content-Type': 'application/json'})
    
    
    #EJ5
    @app.route('/age/<dob>')
    def calculate_age(dob):
        response = {
            "edad": calcular_edad(dob)
        }
        
        if response["edad"] == -1:
            return ({"error": "Error en la APP"}, 400, {'Content-Type': 'application/json'})
        else:
            return (response, 200, {'Content-Type': 'application/json'})
        
                
        
        
    #EJ6
    @app.route('/operate/<string:operation>/<int:num1>/<int:num2>')
    def operation_resquest(operation, num1, num2):
        response = {
            "resultado": None
        }
        
        if operation == "sum":
            response["resultado"] = num1 + num2
            return (response, 200, {'Content-Type': 'application/json'})
        elif operation == "sub":
            response["resultado"] = num1 - num2
            return (response, 200, {'Content-Type': 'application/json'})
        elif operation == "mult":
            response["resultado"] = num1 * num2
            return (response, 200, {'Content-Type': 'application/json'})
        elif operation == "div":
            if num2 != 0:
                response["resultado"] = num1 / num2
                return (response, 200, {'Content-Type': 'application/json'})
            else:
                return ({"error": "Division entre 0"}, 400, {'Content-Type': 'application/json'})
        
        else:
            return ({"error": "Error en la APP"}, 400, {'Content-Type': 'application/json'})
        
        from flask import request
        
        
    #EJ7
    @app.route('/operate')
    def operation_request_query():
        operation = request.args.get('operation')
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))

        response = {
            "resultado": None
        }

        if operation == "sum":
            response["resultado"] = num1 + num2
            return (response, 200, {'Content-Type': 'application/json'})
        elif operation == "sub":
            response["resultado"] = num1 - num2
            return (response, 200, {'Content-Type': 'application/json'})
        elif operation == "mult":
            response["resultado"] = num1 * num2
            return (response, 200, {'Content-Type': 'application/json'})
        elif operation == "div":
            if num2 != 0:
                response["resultado"] = num1 / num2
                return (response, 200, {'Content-Type': 'application/json'})
            else:
                return ({"error": "Division entre 0"}, 400, {'Content-Type': 'application/json'})
        else:
            return ({"error": "Error en la APP"}, 400, {'Content-Type': 'application/json'})
        
        
        
    #EJ8
    @app.route('/title/<string:word>')
    def format_title_libro(word):

        response = {
            "titulo": format_title_case(word)
        }
        return (response, 200, {'Content-Type': 'application/json'})
    
    
    
    #EJ9
    @app.route('/formatted/<string:dni>')
    def convertir_dni(dni):
        dni_convertido = quitar_signos(dni)
        resultado = {"formatted_dni":dni_convertido}
        return jsonify(resultado)
    
    
    
    #EJ10
    @app.route('/format')
    def format_user_data():
        
        firstname = request.args.get('firstname')
        lastname = request.args.get('lastname')
        dob = request.args.get('dob')
        dni = request.args.get('dni')        
        
        formatted_firstname = format_name(firstname)
        formatted_lastname = format_name(lastname)        
        
        dob_date = datetime.strptime(dob, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))        
        
        dni_numeric = validate_dni(dni)
        if dni_numeric is None:
            error_message = {'error': 'El DNI no es válido'}
            return jsonify(error_message), 400        
        
        response = {
            'firstname': formatted_firstname,
            'lastname': formatted_lastname,
            'age': age,
            'dni': dni_numeric
        }
        
        return jsonify(response)
    


#EJ11

    with open('morse_code.json') as file:
     morse_code_dict = json.load(file)['letters']
   
    def encode_to_morse(keyword):
        morse_encoded = []
        for char in keyword:
            if char == '+':
                morse_encoded.append('^')
            else:
                morse_encoded.append(morse_code_dict.get(char, char))
        return '+'.join(morse_encoded)
    
    @app.route('/encode/<string:keyword>')
    def encode_keyword(keyword):        
        keyword = keyword.replace('^', ' ')        
        if not keyword.isalnum() or len(keyword) > 100:
            error_message = {'error': 'Palabra clave no válida'}
            return jsonify(error_message), 400
        
        morse_encoded = encode_to_morse(keyword.upper())
        response = {'morse_encoded': morse_encoded}
        
        return jsonify(response)
    


    #EJ12
    with open('morse_code.json') as file:
     morse_code_dict = json.load(file)['letters']

    def decode_from_morse(morse_code):
        morse_parts = morse_code.split('+')
        decoded = []
        for part in morse_parts:
            char = next((key for key, value in morse_code_dict.items() if value == part), None)
            if char is not None:
                decoded.append(char)
            elif part == '^':
                decoded.append(' ')
        return ''.join(decoded)

    @app.route('/decode/<string:morse_code>')
    def decode_morse_code(morse_code):
        plaintext = decode_from_morse(morse_code)
        response = {'plaintext': plaintext}
        
        return jsonify(response)
    


    #EJ13
    @app.route('/convert/binary/<string:num>')
    def convert_binary(num):
        if not all(bit in ['0', '1'] for bit in num):
            error_message = {'error': 'Número binario inválido'}
            return jsonify(error_message), 400
        
        decimal_result = convert_binary_to_decimal(num)
        response = {'decimal': decimal_result}
        
        return jsonify(response)
    


    #EJ14
    @app.route('/balance/<string:input>')
    def check_balance(input):
        if is_balanced(input):
            response = {'balanced': True}
        else:
            response = {'balanced': False}
        
        return jsonify(response)



    
    @app.route('/academia/<string:user>')
    def academia(user):
        return f'Bienvenido a la academia! {user}'
    
    @app.get('/login')
    def login_get():
        return render_template("formulario_login.html")
    return app
