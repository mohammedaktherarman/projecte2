document.getElementById("register-btn").addEventListener("click", async function () {
    const userType = document.getElementById("user-type").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const endpoint = userType === "empresa" ? "/empresa/" : "/influencer/";
    const userData = { email, password };

    try {
        const response = await fetch(`http://localhost:8000${endpoint}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(userData)
        });

        const result = await response.json();
        if (response.ok) {
            alert(result.message || "Registro completado");
            window.location.href = "../login/login.html";
        } else {
            alert(result.detail || result.message || "Error en el registro");
        }
    } catch (error) {
        console.error("Error al conectar con el servidor:", error);
        alert("Error al conectar con el servidor");
    }
});
