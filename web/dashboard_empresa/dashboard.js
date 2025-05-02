// Función para cambiar de sección
function showSection(section) {
  document.getElementById('perfil').classList.add('hidden');
  document.getElementById('buscar').classList.add('hidden');
  document.getElementById('guardados').classList.add('hidden');
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
          <div class="border rounded p-4 shadow hover:shadow-lg transition flex items-center">
            <img src="${influencer.imagen || 'https://via.placeholder.com/100'}" alt="Foto" class="rounded-full w-20 h-20 mb-2">
            <div class="ml-4 flex-1"> <!-- Espaciado entre la imagen y el texto -->
              <h3 class="font-bold">${influencer.nom}</h3>
              <p class="text-sm text-gray-600">Categoría: ${influencer.sector}</p>
              <p class="text-sm text-gray-600">Seguidores: ${influencer.seguidores}</p>
              <a href="#" class="text-blue-600 text-sm" onclick="showProfile(${influencer.id_influencer})">Ver perfil completo</a>
            </div>
            <!-- El ícono de guardar ahora está alineado a la derecha -->
            <i class="fa fa-bookmark text-gray-600 hover:text-blue-600 cursor-pointer ml-auto" onclick="saveInfluencer(${influencer.id_influencer})"></i>
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
            <h2 class="text-2xl font-bold">${influencer.nom}</h2> <!-- Cambiado de 'nombre' a 'nom' -->
            <p class="text-sm text-gray-600">📍 ${influencer.ubicacio}</p> <!-- Cambiado de 'ubicacion' a 'ubicacio' -->
          </div>
        </div>
        <div class="mb-4">
          <span class="inline-block bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm mr-2">${influencer.sector}</span>
        </div>
        <p class="mb-4 text-gray-700"><strong>Seguidores:</strong> ${influencer.seguidores}</p>
        <div class="mb-6">
          <h3 class="text-lg font-semibold mb-1">Sobre mí</h3>
          <p>${influencer.descripcio}</p> <!-- Cambiado de 'descripcion' a 'descripcio' -->
        </div>
        <div class="bg-gray-50 p-4 rounded">
          <p class="text-sm">¿Te interesa colaborar con ${influencer.nom}?</p> <!-- Cambiado de 'nombre' a 'nom' -->
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

// Función para guardar el influencer
function saveInfluencer(id) {
  const savedList = JSON.parse(localStorage.getItem('savedInfluencers')) || [];
  if (!savedList.includes(id)) {
    savedList.push(id);
    localStorage.setItem('savedInfluencers', JSON.stringify(savedList));
    alert('Influencer guardado con éxito');
    loadSavedInfluencers();  // Actualizar la sección de guardados inmediatamente
  } else {
    alert('Este influencer ya está guardado');
  }
}

// Función para cargar los influencers guardados
function loadSavedInfluencers() {
  const savedList = JSON.parse(localStorage.getItem('savedInfluencers')) || [];
  const savedListContainer = document.getElementById('saved-list');
  savedListContainer.innerHTML = '';

  if (savedList.length === 0) {
    savedListContainer.innerHTML = '<p>No tienes influencers guardados.</p>';
  }

  savedList.forEach(id => {
    fetch(`http://localhost:8000/influencer/${id}`)
      .then(response => response.json())
      .then(data => {
        if (data.status === 'ok') {
          const influencer = data.data;
          const savedCard = `
            <div class="border rounded p-4 shadow hover:shadow-lg transition flex items-center">
              <img src="${influencer.imagen || 'https://via.placeholder.com/100'}" alt="Foto" class="rounded-full w-20 h-20 mb-2">
              <div class="ml-4 flex-1">
                <h3 class="font-bold">${influencer.nom}</h3>
                <p class="text-sm text-gray-600">Categoría: ${influencer.sector}</p>
                <p class="text-sm text-gray-600">Seguidores: ${influencer.seguidores}</p>
                <a href="#" class="text-blue-600 text-sm" onclick="showProfile(${influencer.id_influencer})">Ver perfil completo</a>
              </div>
            </div>
          `;
          savedListContainer.innerHTML += savedCard;
        }
      })
      .catch(error => console.error('Error loading saved influencer:', error));
  });
}

// Cargar los influencers y los datos de la empresa al cargar la página
window.onload = () => {
  loadInfluencers();
  loadSavedInfluencers(); // Cargar los influencers guardados al iniciar la página
};
