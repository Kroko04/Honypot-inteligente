from flask import Flask, request

app = Flask(__name__)

# VULNERABILIDAD 1: Contraseña en texto plano (Hardcoded password)
SECRET_ADMIN_PASS = "admin1234_super_segura"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('username')
        clave = request.form.get('password')

        # Guardamos el intento en un archivo de texto
        with open("intentos_hackeo.log", "a") as archivo:
            archivo.write(f"Intento - Usuario: {usuario}, Clave: {clave}\n")

     
        if clave == SECRET_ADMIN_PASS:
            return "¡Bienvenido al sistema secreto!"
        else:
            return "Acceso denegado. Intento registrado."

    return '''
        <h2>Panel de Administrador Confidencial</h2>
        <form method="POST">
            Usuario: <input type="text" name="username"><br><br>
            Contraseña: <input type="password" name="password"><br><br>
            <input type="submit" value="Entrar">
        </form>
    '''

if __name__ == '__main__':
    # VULNERABILIDAD 2: Binding a todas las interfaces sin protección
    app.run(host='0.0.0.0', port=8080)
