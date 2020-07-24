var tableRef = document.getElementById('expenseTable').getElementsByTagName('tbody')[document.getElementById('expenseTable').getElementsByTagName('tbody').length -1];

var newRow = tableRef.insertRow(tableRef.rows.length);

var newCell = newRow.insertCell(0);
var newCell1 = newRow.insertCell(1);
var newCell2 = newRow.insertCell(2);
var newCell3 = newRow.insertCell(3);

var newText = document.createTextNode('New Row')

newCell.appendChild(newText);
newCell1.appendChild(newText);
newCell2.appendChild(newText);
newCell.appendChild(newText);

newCell.style.border = "1px solid black"; 
newCell1.style.border = "1px solid black"; 
newCell2.style.border = "1px solid black"; 
newCell3.style.border = "1px solid black"; 
