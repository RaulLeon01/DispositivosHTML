# INSTALACIÓN DE FLASK:
# 1. cd C:/Users/TuUsuario/Documents/Flask_
# 2. python -m venv venv
# 3. venv\Scripts\activate
# 4. pip install flask
# 5. pip show flask
# 6. python app.py

from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder='src', static_url_path='')

# Almacenamiento en memoria
dispositivos_registrados = []

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Listar dispositivos
@app.route('/api/dispositivos', methods=['GET'])
def api_listar_dispositivos():
    return jsonify(dispositivos_registrados), 200

# Agregar dispositivo (básico)
@app.route('/api/dispositivos', methods=['POST'])
def api_agregar_dispositivo():
    payload = request.get_json(silent=True) or {}
    dispositivo = {
        'sid': (payload.get('sid') or '').strip(),
        'nombre': (payload.get('nombre') or '').strip(),
        'ip': (payload.get('ip') or '').strip(),
        'protocolos': [p.strip() for p in (payload.get('protocolos') or '').split(',')] if payload.get('protocolos') else [],
        'observaciones': (payload.get('observaciones') or '').strip()
    }
    dispositivos_registrados.append(dispositivo)
    return jsonify({'mensaje': 'Dispositivo agregado', 'dispositivo': dispositivo}), 201

if __name__ == '__main__':
    app.run(debug=True)
