document.addEventListener("DOMContentLoaded", function () {
  const userId = localStorage.getItem("userId");
  const userType = localStorage.getItem("userType");

  if (!userId || !userType) {
    alert("No se ha encontrado información de usuario.");
    return;
  }

  const endpoint = userType === "empresa" ? `/empresa/${userId}` : `/influencer/${userId}`;

  fetch(`http://54.236.163.28${endpoint}`)
    .then(response => response.json())
    .then(result => {
      if (result && result.data) {
        const mappedData = mapKeys(result.data);
        fillForm(mappedData);
        loadPreview(mappedData);
      }
    })
    .catch(error => {
      console.error("Error al obtener los datos:", error);
      alert("Error al cargar los datos del perfil.");
    });

  function mapKeys(data) {
    return {
      nombre: data.nombre || data.nom || "",
      descripcion: data.descripcion || data.descripcio || "",
      imagen: data.imagen || "",
      email_contacto: data.email_contacto || "",
      telefono: data.telefono || data.telefon || "",
      sector: data.sector || "",
      redsocial: data.redsocial || "",
      seguidores: data.seguidores || "",
      ubicacion: data.ubicacion || data.ubicacio || "",
      web: data.web || data.web_empresa || "",
      link: data.link || ""
    };
  }

  function fillForm(data) {
    document.getElementById("nombre").value = data.nombre;
    document.getElementById("descripcion").value = data.descripcion;
    document.getElementById("imagen").value = data.imagen;
    document.getElementById("email_contacto").value = data.email_contacto;
    document.getElementById("telefono").value = data.telefono;
    document.getElementById("sector").value = data.sector;
    document.getElementById("redsocial").value = data.redsocial;
    document.getElementById("seguidores").value = data.seguidores;
    document.getElementById("ubicacion").value = data.ubicacion;
  }

  function loadPreview(data) {
    const previewContent = `
      <div class="flex items-center space-x-4 mb-6">
        <img src="${data.imagen || 'https://via.placeholder.com/100'}" alt="Foto" class="rounded-full w-24 h-24">
        <div>
          <h2 class="text-2xl font-bold">${data.nombre}</h2>
          <p class="text-sm text-gray-600">📍 ${data.ubicacion}</p>
        </div>
      </div>
      <p class="mb-4 text-gray-700"><strong>Seguidores:</strong> ${data.seguidores}</p>
      <div class="mb-6">
        <h3 class="text-lg font-semibold mb-1">Sobre mí</h3>
        <p>${data.descripcion}</p>
      </div>
      <div class="mb-6">
        <h3 class="text-lg font-semibold mb-1">Redes sociales</h3>
        <ul class="space-y-1">
          <li><a href="${data.redsocial}" target="_blank" class="text-blue-600 hover:underline">${data.redsocial}</a></li>
        </ul>
      </div>
      <div class="bg-gray-50 p-4 rounded">
        <p class="text-sm">¿Te interesa colaborar?</p>
        <p class="font-medium mt-1">📧 ${data.email_contacto}</p>
        <p class="font-medium mt-1">📞 ${data.telefono}</p>
      </div>
    `;
    document.getElementById("preview-content").innerHTML = previewContent;
  }

  document.getElementById("btn-vista-previa").addEventListener("click", function (e) {
    e.preventDefault();
    document.getElementById("editar").classList.add("hidden");
    document.getElementById("preview").classList.remove("hidden");

    fetch(`http://54.236.163.28${endpoint}`)
      .then(response => response.json())
      .then(result => {
        if (result && result.data) {
          const mappedData = mapKeys(result.data);
          loadPreview(mappedData);
        }
      });
  });

  document.getElementById("btn-editar").addEventListener("click", function (e) {
    e.preventDefault();
    document.getElementById("editar").classList.remove("hidden");
    document.getElementById("preview").classList.add("hidden");
  });

  document.getElementById("edit-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const data = {
      nombre: document.getElementById("nombre").value.trim(),
      descripcion: document.getElementById("descripcion").value.trim(),
      imagen: document.getElementById("imagen").value.trim(),
      email_contacto: document.getElementById("email_contacto").value.trim(),
      telefono: document.getElementById("telefono").value.trim(),
      sector: document.getElementById("sector").value.trim(),
      redsocial: document.getElementById("redsocial").value.trim(),
      seguidores: document.getElementById("seguidores").value.trim(),
      ubicacion: document.getElementById("ubicacion").value.trim(),
    };

    try {
      const response = await fetch(`http://54.236.163.28${endpoint}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });

      const result = await response.json();

      if (response.ok) {
        alert("Perfil actualizado correctamente. Mira cómo queda en Vista previa");
        loadPreview(data);
      } else {
        alert(result.detail || "Error al actualizar el perfil.");
      }
    } catch (error) {
      console.error(error);
      alert("Conexión a la API fallida");
    }
  });
});

function cerrarSesion() {
  localStorage.clear();
  window.location.href = "../login/login.html";
}
