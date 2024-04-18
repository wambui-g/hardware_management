function showPopupForm() {
    document.getElementById("popupForm").style.display = "block";
}

function hidePopupForm() {
    document.getElementById("popupForm").style.display = "none";
}

function addItem() {
    var category = document.getElementById("categoryInput").value;
    var subCategory = document.getElementById("subCategoryInput").value;
    var item = document.getElementById("itemInput").value;
    var count = document.getElementById("countInput").value;

    var newRow = document.createElement("div");
    newRow.classList.add("added-item-row");

    var inputs = [category, subCategory, item, count];
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

