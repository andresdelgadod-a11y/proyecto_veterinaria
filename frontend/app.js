const URL_API = 'http://127.0.0.1:8000/api/mascotas/';
const tabla = document.getElementById('tabla');
const formulario = document.getElementById('formulario');

// GET: trae las mascotas y las pinta en la tabla
async function cargarMascotas() {
  const respuesta = await fetch(URL_API);
  const mascotas = await respuesta.json();
  tabla.innerHTML = '';
  mascotas.forEach(m => {
    tabla.innerHTML += `
      <tr>
        <td>${m.id}</td><td>${m.nombre}</td><td>${m.especie}</td>
        <td>${m.raza}</td><td>${m.edad}</td><td>${m.dueno}</td>
      </tr>`;
  });
}

// POST: envía el formulario y recarga la tabla sin refrescar la página
formulario.addEventListener('submit', async (e) => {
  e.preventDefault();
  const datos = Object.fromEntries(new FormData(formulario));
  const respuesta = await fetch(URL_API, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(datos)
  });
  if (respuesta.ok) {
    formulario.reset();
    cargarMascotas();
  } else {
    alert('Error: ' + JSON.stringify(await respuesta.json()));
  }
});

cargarMascotas();