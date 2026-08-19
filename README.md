# Proyecto de ejemplo: API + Página web

Una lista de tareas simple, dividida en dos partes independientes que se
comunican entre sí. Así funciona la gran mayoría de las aplicaciones web reales.

## Estructura

```
proyecto-ejemplo/
├── backend/
│   ├── app.py             → la API (Python + Flask)
│   └── requirements.txt   → dependencias que hay que instalar
└── frontend/
    ├── index.html          → estructura de la página
    ├── style.css           → estilos
    └── script.js           → se comunica con la API
```

## Cómo correrlo

1. **Levantar la API:**
   ```
   cd backend
   pip install -r requirements.txt
   python app.py
   ```
   Esto deja la API escuchando en `http://localhost:5000`.

2. **Abrir la página:** doble click en `frontend/index.html` (o servila con
   la extensión "Live Server" de VS Code). El JavaScript va a llamar a la API
   que dejaste corriendo en el paso 1.

3. Probá agregar una tarea y hacer click sobre una para marcarla como hecha.

## El flujo completo, en criollo

1. Abrís `index.html` en el navegador → eso es la "página web".
2. `script.js` hace `fetch()` hacia `http://localhost:5000/api/tareas` → eso es
   "consumir la API".
3. `app.py` recibe esa petición, busca en `tareas` (la lista en memoria) y
   responde con JSON.
4. `script.js` recibe ese JSON y arma el HTML con las tareas.

La API no sabe nada de HTML ni de diseño. La página no sabe nada de cómo se
guardan los datos. Cada una hace su trabajo y se comunican por HTTP + JSON.
Esa separación es la base de casi todo backend/frontend moderno.
