document.addEventListener("click", function(event) {
    var dropdownContent = document.getElementById("user-dropdown-content");
    var dropdownButton = document.querySelector(".dropbtn");

    // If the clicked element is not the dropdown button or its content, hide the dropdown
    if (!dropdownContent.contains(event.target) && event.target !== dropdownButton) {
        dropdownContent.style.display = "none";
    }
});

function showDropDown() {
    var dropdownContent = document.getElementById("user-dropdown-content");
    dropdownContent.style.display = (dropdownContent.style.display === "block") ? "none" : "block";
}