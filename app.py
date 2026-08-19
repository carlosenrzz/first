from flask import Flask, jsonify, request
from flask_cors import CORS

# --- Qué es esto ---
# Flask es un "microframework": un conjunto de herramientas mínimas para
# levantar un servidor que escucha peticiones HTTP y responde.
app = Flask(__name__)

# CORS permite que un frontend que corre en otro origen (otro puerto/dominio)
# pueda llamar a esta API sin que el navegador lo bloquee por seguridad.
CORS(app)

# "Base de datos" en memoria: se reinicia cada vez que reiniciás el servidor.
# En un proyecto real esto sería una base de datos de verdad (PostgreSQL, etc).
tareas = [
    {"id": 1, "texto": "Entender qué es una API", "hecha": True},
    {"id": 2, "texto": "Crear mi primera API con Flask", "hecha": False},
]

# --- ENDPOINTS ---
# Un "endpoint" es una URL + un método HTTP que hace algo específico.

@app.route("/api/tareas", methods=["GET"])
def obtener_tareas():
    """GET = pedir datos. Devuelve la lista completa de tareas."""
    return jsonify(tareas)

@app.route("/api/tareas", methods=["POST"])
def crear_tarea():
    """POST = crear algo nuevo. Recibe JSON del cliente y agrega una tarea."""
    datos = request.get_json()
    nueva = {
        "id": len(tareas) + 1,
        "texto": datos["texto"],
        "hecha": False
    }
    tareas.append(nueva)
    return jsonify(nueva), 201  # 201 = "creado correctamente"

@app.route("/api/tareas/<int:tarea_id>", methods=["PATCH"])
def marcar_hecha(tarea_id):
    """PATCH = modificar algo que ya existe. Cambia el estado hecha/no hecha."""
    for t in tareas:
        if t["id"] == tarea_id:
            t["hecha"] = not t["hecha"]
            return jsonify(t)
    return jsonify({"error": "tarea no encontrada"}), 404  # 404 = "no existe"

if __name__ == "__main__":
    # debug=True reinicia el servidor solo cuando cambiás el código
    app.run(debug=True, port=5000)
