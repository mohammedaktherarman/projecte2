document.getElementById("login-form").addEventListener("submit", async function (event) {
    event.preventDefault(); 

    const userType = document.getElementById("user-type").value;
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (!username || !password) {
        return; 
    }

    const endpoint = userType === "empresa" ? "/empresa/login" : "/influencer/login";
    const loginData = { email: username, password };

    try {
        const response = await fetch(`/api${endpoint}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(loginData)
        });

        const result = await response.json();
        if (response.ok) {
            localStorage.clear();
            
            if (userType === "empresa") {
                localStorage.setItem("userId", result.user.id_empresa);
                localStorage.setItem("userType", "empresa");
                window.location.href = "../dashboard_empresa/dashboard.html";
            } else {
                localStorage.setItem("userId", result.user.id_influencer);
                localStorage.setItem("userType", "influencer");
                window.location.href = "../dashboard_influencer/dashboard.html";
            }
        } else {
            alert(result.detail || result.missatge || "Credenciales incorrectas");
        }
    } catch (error) {
        console.error("Error al conectar con el servidor:", error);
        alert("Conexión a la API fallida");
    }
});
