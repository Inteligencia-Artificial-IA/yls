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
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('message').lower()
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Buscar en la columna de keywords
    cursor.execute("SELECT respuesta FROM preguntas WHERE LOWER(keywords) LIKE %s", ('%' + user_input + '%',))
    result = cursor.fetchone()
    
    if not result:
        # Buscar en la columna de preguntas si no se encuentra en keywords
        cursor.execute("SELECT respuesta FROM preguntas WHERE LOWER(pregunta) LIKE %s", ('%' + user_input + '%',))
        result = cursor.fetchone()
    
    if result:
        response = result['respuesta']
    else:
        response = predict_response(user_input)
    
    cursor.close()
    connection.close()
    return jsonify({'response': response})

def predict_response(user_input):
    responses = {
        'prácticas pre profesionales': (
            "Las Prácticas Pre Profesionales (PPP) son parte del proceso formativo en la Escuela Profesional de Ingeniería de Sistemas "
            "de la UAC. Para más información, consulta los planes de estudio 2013, 2016 y 2020."
        ),
        'horario de atención': (
            "La atención para el ING 413 es los lunes y martes de 2:00pm a 4:00pm, y los jueves y viernes de 7:00am a 9:00am."
        ),
        'grupo de whatsapp': (
            "Puedes unirte al grupo de WhatsApp para obtener más información en el siguiente enlace: "
            "<a href='https://chat.whatsapp.com/EQEBN6eAhOc6W3CVKULsed' target='_blank'>Unirme al grupo de WhatsApp</a>."
        ),
        'reconocimiento del ejercicio pre profesional': (
            "El trámite para el reconocimiento del Ejercicio Pre Profesional se realiza por mesa de partes virtual. "
            "Debes solicitar RECONOCIMIENTO DEL EJERCICIO PRE PROFESIONAL, adjuntando el recibo de pago (código C33290001), "
            "el informe final y tu carta de presentación."
        ),
        'información adicional': (
            "Para más detalles, visita el sitio web de la UAC: "
            "<a href='https://sites.google.com/view/pppsistemasuac/inicio?authuser=0' target='_blank'>Sitio oficial de la UAC</a>."
        )
    }
    
    for keyword, response in responses.items():
        if keyword in user_input:
            return response
    
    return (
        "Lo siento, no tengo una respuesta específica para esa pregunta. "
        "Por favor, consulta el <a href='https://sites.google.com/view/pppsistemasuac/inicio?authuser=0' target='_blank'>sitio web de la UAC</a> "
        "o contacta a la Facultad de Ingeniería y Arquitectura para más información."
    )

if __name__ == '__main__':
    app.run(debug=True)
