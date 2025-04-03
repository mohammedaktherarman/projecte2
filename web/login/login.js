document.getElementById("login-btn").addEventListener("click", async function () {
    const userType = document.getElementById("user-type").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const endpoint = userType === "empresa" ? "/empresa/login" : "/influencer/login";
    const loginData = { email: username, password };

    try {
        const response = await fetch(`http://localhost:8000${endpoint}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(loginData)
        });

        const result = await response.json();
        if (response.ok) {
            alert("Inicio de sesión exitoso");
            window.location.href = "/web/main/inicio.html"; 
        } else {
            alert(result.missatge || "Credenciales incorrectas");
        }
    } catch (error) {
        alert("Error al conectar con el servidor");
    }
});
