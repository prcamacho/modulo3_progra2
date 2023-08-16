from flask import Flask, request
from config import Config

from .utils.utilstp3 import calcular_edad, format_title_case

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



             
    
    
    @app.route('/academia/<string:user>')
    def academia(user):
        return f'Bienvenido a la academia! {user}'
    
    @app.get('/login')
    def login_get():
        return render_template("formulario_login.html")
    return app
