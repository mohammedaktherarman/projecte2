document.getElementById("register-btn").addEventListener("click", async function () {
    const userType = document.getElementById("user-type").value;
    const nombre = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const telefono = document.getElementById("phone").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm-password").value;

    if (password !== confirmPassword) {
        alert("Las contraseñas no coinciden");
        return;
    }

    const endpoint = userType === "empresa" ? "/empresa/" : "/influencer/";
    const userData = { nombre, email, telefono, password };

    try {
        const response = await fetch(`http://localhost:8000${endpoint}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(userData)
        });

        const result = await response.json();
        if (response.ok) {
            window.location.href = "/web/login/login.html";
        } else {
            alert(result.detail || "Error en el registro");
        }
    } catch (error) {
        alert("Error al conectar con el servidor");
    }
});
