function showMessage(message) {
    alert(message);
}

function validateRegister() {
    let password = document.getElementById("password").value;

    if (password.length < 6) {
        alert("Password must be at least 6 characters");
        return false;
    }

    alert("Registration Successful!");
    return true;
}

function validateLogin() {
    alert("Login Successful!");
    return true;
}