// script.js - Code test validation
document.addEventListener('DOMContentLoaded', function() {
    console.log("✅ JavaScript loaded successfully!");
    
    const loginForm = document.getElementById('loginForm');
    
    if (loginForm) {
        console.log("✅ Form found!");
        
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();
            console.log("✅ Form submitted!");
            
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            
            console.log("Username:", username);
            console.log("Password:", password);
            
            // Test validation
            if (validateLogin(username, password)) {
                console.log("✅ Login validation passed!");
                alert("Đăng nhập thành công!");
            } else {
                console.log("❌ Login validation failed!");
            }
        });
    } else {
        console.log("❌ Form not found! Check HTML structure.");
    }
});

function validateLogin(username, password) {
    if (username === "") {
        console.log("Username is empty");
        return false;
    }
    
    if (password === "") {
        console.log("Password is empty");
        return false;
    }
    
    if (password.length < 6) {
        console.log("Password too short");
        return false;
    }
    
    return true;
}