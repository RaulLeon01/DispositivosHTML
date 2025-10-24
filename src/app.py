from flask import Flask, jsonify, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Lista para almacenar los dispositivos
dispositivos_registrados = []

@app.route('/formulario')
def formulario():
    return render_template_string("""
    <html>
    <head><title>Agregar Dispositivo</title></head>
    <body>
        <h1>Nuevo Dispositivo</h1>
        /agregar
            SID: <input type="text" name="sid"><br>
            Nombre: <input type="text" name="nombre"><br>
            IP: <input type="text" name="ip"><br>
            Protocolos (separados por coma): <input type="text" name="protocolos"><br>
            Observaciones: <input type="text" name="observaciones"><br>
            <input type="submit" value="Agregar">
        </form>
    </body>
    </html>
    """)

@app.route('/agregar', methods=['POST'])
def agregar_dispositivo():
    data = {
        "sid": request.form['sid'],
        "nombre": request.form['nombre'],
        "ip": request.form['ip'],
        "protocolos": [p.strip() for p in request.form['protocolos'].split(',')],
        "observaciones": request.form['observaciones']
    }
    dispositivos_registrados.append(data)
    return redirect(url_for('mostrar_dispositivos'))

@app.route('/dispositivos')
def mostrar_dispositivos():
    html = ""
    for d in dispositivos_registrados:
        html += f"""
        <div style="border:1px solid #ccc; padding:10px; margin:10px;">
            <strong>{d['sid']}</strong><br>
            <b>Nombre:</b> {d['nombre']}<br>
            <b>IP:</b> {d['ip']}<br>
            <b>Protocolos:</b> {', '.join(d['protocolos'])}<br>
            <b>Observaciones:</b> {d['observaciones']}
        </div>
        """

    return render_template_string(f"""
    <html>
    <head><title>Dispositivos de Red</title></head>
    <body>
        <h1>Lista de Dispositivos</h1>
        /formularioAgregar nuevo dispositivo</a>
        {html}
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)