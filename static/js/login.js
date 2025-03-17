function togglePassword() {
    const passwordInput = document.getElementById('login-password');
    const toggleIcon = document.getElementById('toggle-password');
    
    if (passwordInput.type === 'password') {
      passwordInput.type = 'text';
      toggleIcon.className = 'ri-eye-off-line login__eye';
    } else {
      passwordInput.type = 'password';
      toggleIcon.className = 'ri-eye-line login__eye';
    }
  }