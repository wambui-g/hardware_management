/* homepage.js */
function addNewItem(boxId) {
    const table = document.getElementById(boxId).querySelector('table');
    const newRow = table.insertRow(-1);
    newRow.innerHTML = `
        <td><input type="text" placeholder="Sub Category"></td>
        <td><input type="number" placeholder="0"></td>
    `;
}

/* inventory.js */
function addRow() {
    var newRow = document.createElement("div");
    newRow.classList.add("row");

    var commands = ["Category", "Sub-Category", "Item", "Count"];
    for (var i = 0; i < commands.length; i++) {
        var input = document.createElement("input");
        input.setAttribute("type", "text");
        input.classList.add("command");
        input.placeholder = "Enter " + commands[i];
        newRow.appendChild(input);
    }

    document.querySelector(".container").insertBefore(newRow, document.querySelector(".add-row-btn"));
}

function saveInventory() {
    // Add your save functionality here
    alert("Inventory saved!");
}

/* invoice.js */
function addInvoiceRow() {
    var formRow = document.createElement('div');
    formRow.className = 'form-row';
    formRow.innerHTML = `
        <div class="form-item">
            <input type="text" placeholder="Enter invoice number">
        </div>
        <div class="form-item">
            <input type="text" placeholder="Enter sub-category">
        </div>
        <div class="form-item">
            <input type="text" placeholder="Enter item">
        </div>
        <div class="form-item">
            <input type="text" placeholder="Enter fulfilment">
        </div>
        <div class="form-item">
            <input type="date">
        </div>
    `;
    document.querySelector('.form-rows').appendChild(formRow);
}

function saveInvoice() {
    var inputs = document.querySelectorAll('.form-item input');
    var invoiceData = {};
    inputs.forEach(function(input, index) {
        var key = input.placeholder.split(' ').join('_').toLowerCase();
        var value = input.value;
        invoiceData[key] = value;
    });
    console.log(invoiceData);
}

document.getElementById('addRowBtn').addEventListener('click', addInvoiceRow);

document.getElementById('saveBtn').addEventListener('click', saveInvoice);

/* login.js */
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    // Simulate login request
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    // Replace this with your actual login logic
    console.log('Email:', email);
    console.log('Password:', password);
});

/* signup.js */
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

/* reports.js */
function addRow() {
    var newRow = document.createElement("div");
    newRow.classList.add("row");

    var commands = ["SALES REPORTS", "MONTHLY", "QUARTERLY", "ANNUALLY"];
    for (var i = 0; i < commands.length; i++) {
        var input = document.createElement("input");
        input.setAttribute("type", "text");
        input.classList.add("command");
        input.placeholder = "Enter " + commands[i];
        newRow.appendChild(input);
    }

    document.querySelector(".container").insertBefore(newRow, document.querySelector(".add-row-btn"));
}

function saveReports() {
    // Add your save functionality here
    alert("Reports saved!");
}

