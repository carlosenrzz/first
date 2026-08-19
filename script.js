// URL de la API ya desplegada en Render. Reemplazá esto por TU URL real
// (la que Render te dio al terminar el despliegue).
const API_URL = "https://lista-tareas-api.onrender.com/api/tareas";

const lista = document.getElementById("lista-tareas");
const form = document.getElementById("form-tarea");
const input = document.getElementById("input-texto");

// Pide las tareas a la API y las dibuja en pantalla
async function cargarTareas() {
  const respuesta = await fetch(API_URL);       // hace la petición GET
  const tareas = await respuesta.json();         // convierte la respuesta (JSON) a objeto JS

  lista.innerHTML = "";
  tareas.forEach(tarea => {
    const li = document.createElement("li");
    li.textContent = tarea.texto;
    if (tarea.hecha) li.classList.add("hecha");

    // Al hacer click, avisa a la API que cambie el estado
    li.addEventListener("click", () => marcarHecha(tarea.id));

    lista.appendChild(li);
  });
}

// Envía una tarea nueva a la API (POST)
async function crearTarea(texto) {
  await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ texto })
  });
  cargarTareas(); // vuelve a pedir la lista actualizada
}

// Marca una tarea como hecha/no hecha (PATCH)
async function marcarHecha(id) {
  await fetch(`${API_URL}/${id}`, { method: "PATCH" });
  cargarTareas();
}

form.addEventListener("submit", (evento) => {
  evento.preventDefault(); // evita que la página se recargue
  crearTarea(input.value);
  input.value = "";
});

// Al abrir la página, carga las tareas por primera vez
cargarTareas();
