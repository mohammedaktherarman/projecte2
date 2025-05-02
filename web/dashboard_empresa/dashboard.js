// Función para cambiar de sección
function showSection(section) {
  document.getElementById('perfil').classList.add('hidden');
  document.getElementById('buscar').classList.add('hidden');
  document.getElementById('perfil-completo').classList.add('hidden');
  document.getElementById(section).classList.remove('hidden');
}

// Función para cargar los influencers desde la API
async function loadInfluencers() {
  try {
    const response = await fetch('http://localhost:8000/influencers/');
    const data = await response.json();
    if (data.status === 'ok') {
      const influencers = data.data;
      const influencerList = document.getElementById('influencer-list');
      influencerList.innerHTML = '';
      influencers.forEach(influencer => {
        const influencerCard = `
          <div class="border rounded p-4 shadow hover:shadow-lg transition">
            <img src="${influencer.imagen || 'https://via.placeholder.com/100'}" alt="Foto" class="rounded-full w-20 h-20 mb-2">
            <h3 class="font-bold">${influencer.nombre}</h3>
            <p class="text-sm text-gray-600">Categoría: ${influencer.sector}</p>
            <p class="text-sm text-gray-600">Seguidores: ${influencer.seguidores}</p>
            <a href="#" class="text-blue-600 text-sm" onclick="showProfile(${influencer.id_influencer})">Ver perfil completo</a>
          </div>
        `;
        influencerList.innerHTML += influencerCard;
      });
    }
  } catch (error) {
    console.error('Error fetching influencers:', error);
  }
}

// Función para mostrar el perfil completo del influencer
async function showProfile(id) {
  try {
    const response = await fetch(`http://localhost:8000/influencer/${id}`);
    const data = await response.json();
    if (data.status === 'ok') {
      const influencer = data.data;
      const profileHTML = `
        <div class="flex items-center space-x-4 mb-6">
          <img src="${influencer.imagen || 'https://via.placeholder.com/100'}" alt="Foto" class="rounded-full w-24 h-24">
          <div>
            <h2 class="text-2xl font-bold">${influencer.nombre}</h2>
            <p class="text-sm text-gray-600">📍 ${influencer.ubicacion}</p>
          </div>
        </div>
        <div class="mb-4">
          <span class="inline-block bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm mr-2">${influencer.sector}</span>
        </div>
        <p class="mb-4 text-gray-700"><strong>Seguidores:</strong> ${influencer.seguidores}</p>
        <div class="mb-6">
          <h3 class="text-lg font-semibold mb-1">Sobre mí</h3>
          <p>${influencer.descripcion}</p>
        </div>
        <div class="bg-gray-50 p-4 rounded">
          <p class="text-sm">¿Te interesa colaborar con ${influencer.nombre}?</p>
          <p class="font-medium mt-1">📧 ${influencer.email_contacto}</p>
        </div>
      `;
      document.getElementById('influencer-profile').innerHTML = profileHTML;
      showSection('perfil-completo');
    }
  } catch (error) {
    console.error('Error fetching influencer profile:', error);
  }
}
async function saveChanges() {
  const nombre = document.getElementById('empresa-nombre').value;
  const descripcion = document.getElementById('empresa-descripcion').value;
  const email = document.getElementById('empresa-email').value;
  const ubicacion = document.getElementById('empresa-ubicacion').value;
  const web = document.getElementById('empresa-web').value;

  const userId = localStorage.getItem('userId');
  const userType = localStorage.getItem('userType');

  if (!userId || userType !== 'empresa') {
    alert("No se ha encontrado el ID de la empresa o el tipo de usuario no es empresa. Asegúrate de haber iniciado sesión correctamente.");
    return;
  }

  const empresaData = {
    nombre,
    descripcion,
    email_contacto: email,
    ubicacion,
    web,
  };

  try {
    const response = await fetch(`http://localhost:8000/empresa/${userId}`, {
      method: 'PUT', // Usar PUT para actualización
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(empresaData),
    });

    const data = await response.json();
    if (data.status === 'ok') {
      alert('Perfil actualizado correctamente.');
    } else {
      alert(data.detail || 'Error al actualizar el perfil');
    }
  } catch (error) {
    console.error('Error saving changes:', error);
    alert('Hubo un error al intentar guardar los cambios');
  }
}

// Cargar los influencers al cargar la página
window.onload = loadInfluencers;
