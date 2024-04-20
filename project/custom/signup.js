document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    // Simulate signup request
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    // Replace this with your actual signup logic
    console.log('Name:', name);
    console.log('Email:', email);
    console.log('Password:', password);
});

