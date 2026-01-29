const form = document.getElementById("loginForm");
const errorText = document.getElementById("error");

form.addEventListener("submit", function(e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const humanCheck = document.getElementById("humanCheck").checked;

    if (!humanCheck) {
        errorText.textContent = "Verifikasi manusia dulu.";
        return;
    }

    if (username === "admin" && password === "12345678") {
        window.location.href = "dashboard.html";
    } else {
        errorText.textContent = "Username atau password salah.";
    }
});
