function togglePassword() {
    const passwordInput = document.getElementById('login-password');
    const toggleIcon = document.getElementById('toggle-password');
    
    // Check if the current type of the password input field is 'password'
    if (passwordInput.type === 'password') {
        // If the password is currently hidden, change the type to 'text' to show it
        passwordInput.type = 'text';
        // Change the icon to indicate that the password is now visible
        toggleIcon.className = 'ri-eye-off-line login__eye';
    } else {
        // If the password is currently visible, change the type back to 'password' to hide it
        passwordInput.type = 'password';
        // Change the icon to indicate that the password is now hidden
        toggleIcon.className = 'ri-eye-line login__eye';
    }
}
