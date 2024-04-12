// Function to add a new form row for entering invoice information
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

// Function to save the entered invoice information
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

// Event listener for Add Row button
document.getElementById('addRowBtn').addEventListener('click', addInvoiceRow);

// Event listener for Save button
document.getElementById('saveBtn').addEventListener('click', saveInvoice);

