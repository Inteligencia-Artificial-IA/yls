from flask import Flask, request, jsonify, render_template
import pymysql

app = Flask(__name__)

def get_db_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',  # Cambia la contraseña si es diferente
        database='chatbot_db',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('message', '').lower()
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        # Buscar coincidencias parciales en la columna de keywords
        query = "SELECT respuesta FROM preguntas WHERE LOWER(keywords) LIKE %s"
        cursor.execute(query, ('%' + user_input + '%',))
        result = cursor.fetchone()
        
        if not result:
            # Buscar coincidencias parciales en la columna de preguntas si no se encuentra en keywords
            query = "SELECT respuesta FROM preguntas WHERE LOWER(pregunta) LIKE %s"
            cursor.execute(query, ('%' + user_input + '%',))
            result = cursor.fetchone()
        
        if result:
            response = result['respuesta']
        else:
            response = (
                "Lo siento, no tengo una respuesta específica para esa pregunta. "
                "Por favor, consulta el <a href='https://sites.google.com/view/pppsistemasuac/inicio?authuser=0' target='_blank'>sitio web de la UAC</a> "
                "o contacta a la Facultad de Ingeniería y Arquitectura para más información."
            )
    
    except Exception as e:
        response = f"Ocurrió un error: {str(e)}"
    
    finally:
        cursor.close()
        connection.close()
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
