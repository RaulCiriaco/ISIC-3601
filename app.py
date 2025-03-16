from flask import Flask, jsonify, request
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST']='database' # DEBE SER EL MISMO QUE EL NOMBRE DEL DOCKER-COMPOSE.YAML
app.config['MYSQL_USER']='raulito'
app.config['MYSQL_PASSWORD']='12345'
app.config['MYSQL_DB']='prueba'

mysql = MySQL(app)

# Decorador: En cualquier lenguaje es una funcion sobre otra funcion en la misma linea.
# funcion route: asina caracteristicas para una api
# OCUPA INTERNET PARA INICIAR EL SERVICIO 
# docker-compose down - Detener Servicio
# docker-compose up --build -d Inicializar Servicio
@app.route("/", methods=["GET"])
def get_data():
    try:
        # Crear Conexion
        conexion = mysql.connection.cursor()
        conexion.execute("SELECT * FROM user")
        users = conexion.fetchall()  # Corregir 'fecthall' a 'fetchall'
        result = []
        for user in users:
            result.append({
                "id_user": user[0],
                "username": user[1]
            })
        conexion.close()
        return jsonify(result)  # Corregir 'return' a 'return jsonify(result)'
    except Exception as e:
        return f"Error: {str(e)}"  # Agregar espacio después de 'Error'

@app.route("/<int:id>")
def get_one_by_id(id):
    try:
        conexion = mysql.connection.cursor()
        query = "SELECT * FROM user WHERE id_user = %s"
        conexion.execute(query,(id,))
        user = conexion.fetchone()
        conexion.close()

        if user is None:
            return jsonify({"err":"User not found"}),404
        result = {
            "id_user": user[0],
            "username":user[1]
        }
        return jsonify(result)
    except Exception as e:
        return f"Error: {str(e)}"  # Agregar espacio después de 'Error'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
