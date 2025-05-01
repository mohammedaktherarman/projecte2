function showSection(section) {
    document.getElementById('perfil').classList.add('hidden');
    document.getElementById('buscar').classList.add('hidden');
    document.getElementById('perfil-completo').classList.add('hidden');
    document.getElementById(section).classList.remove('hidden');
  }

  function showProfile() {
    document.getElementById('buscar').classList.add('hidden');
    document.getElementById('perfil-completo').classList.remove('hidden');
  }