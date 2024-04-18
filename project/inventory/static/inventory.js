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

}
