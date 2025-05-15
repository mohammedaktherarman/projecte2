document.getElementById("register-form").addEventListener("submit", async function (event) {
    event.preventDefault();

    const userType = document.getElementById("user-type").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const endpoint = userType === "empresa" ? "/empresa/" : "/influencer/";
    const userData = { email, password };

    try {
        const response = await fetch(`http://54.236.163.28${endpoint}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(userData)
        });

        const result = await response.json();
        if (response.ok) {
            alert("Registrado correctamente");
            window.location.href = "../login/login.html";
        } else {
            alert(result.detail || result.message || "Error en el registro");
        }
    } catch (error) {
        console.error("Error al conectar con el servidor:", error);
        alert("Conexión a la API fallida");
    }
});z
