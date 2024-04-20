function showPopupForm() {
    document.getElementById("popupForm").style.display = "block";
}

function hidePopupForm() {
    document.getElementById("popupForm").style.display = "none";
}

document.getElementById("itemForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the default form submission
    addItem();
});

function addItem() {
    var invoicenumber = document.getElementById("invoicenumberInput").value;
    var subCategory = document.getElementById("subCategoryInput").value;
    var item = document.getElementById("itemInput").value;
    var price = document.getElementById("priceInput").value;
    var count = document.getElementById("countInput").value;
    var invoicedAmount = document.getElementById("invoicedamountInput").value;
    var fulfilment = document.getElementById("fulfilmentInput").value;
    var date = document.getElementById("dateInput").value;

    var newRow = document.createElement("div");
    newRow.classList.add("added-item-row");

    var inputs = [invoicenumber, subCategory, item, price, count, invoicedAmount, fulfilment, date];
    for (var i = 0; i < inputs.length; i++) {
        var input = document.createElement("input");
        input.setAttribute("type", "text");
        input.classList.add("command");
        input.value = inputs[i];
        newRow.appendChild(input);
    }

    document.querySelector(".menu-row").insertAdjacentElement("afterend", newRow);
    hidePopupForm();
}
