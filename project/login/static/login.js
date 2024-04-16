document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    // Simulate login request
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    // Replace this with your actual login logic
    console.log('Email:', email);
    console.log('Password:', password);
});

