function addNewItem(boxId) {
    const table = document.getElementById(boxId).querySelector('table');
    const newRow = table.insertRow(-1);
    newRow.innerHTML = `
        <td><input type="text" placeholder="Sub Category"></td>
        <td><input type="number" placeholder="0"></td>
    `;
}
