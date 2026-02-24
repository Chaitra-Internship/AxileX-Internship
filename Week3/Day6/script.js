//  Alert on Button Click

function showAlert() {
    alert("Button was clicked successfully!");
}

// Form Validation

function validateForm() {

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    if (name === "") {
        alert("Name cannot be empty");
        return false;
    }

    if (email === "") {
        alert("Email cannot be empty");
        return false;
    }

    if (password.length < 6) {
        alert("Password must be at least 6 characters");
        return false;
    }

    alert("Form submitted successfully!");
    return true;
}

// Simple Calculator

function calculate() {

    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    let operator = document.getElementById("operator").value;

    let result;

    if (operator === "+") {
        result = num1 + num2;
    } else if (operator === "-") {
        result = num1 - num2;
    } else if (operator === "*") {
        result = num1 * num2;
    } else if (operator === "/") {
        if (num2 === 0) {
            alert("Cannot divide by zero");
            return;
        }
        result = num1 / num2;
    }

    document.getElementById("result").innerText = "Result: " + result;
}

// Change Text on Click

function changeText() {
    document.getElementById("changeText").innerText =
        "Text has been changed successfully!";
}