
function create_newrow(tableName){

    var MAX_CELL_NUMBER = 4;
    var TAG_ID_ELEMENTS = [tableName+"_name", tableName+"_planned_amount", tableName+"_actual_amount", tableName+"_difference"]
    var COUNT_EXPENSE_TABLE_ELEMENTS = document.getElementById(tableName+'Table').getElementsByTagName('tbody').length -1;

    var table = document.getElementById(tableName+'Table').getElementsByTagName('tbody')[COUNT_EXPENSE_TABLE_ELEMENTS];
    var last_row_number = table.rows.length;
    var newRow = table.insertRow(last_row_number);
    newRow.setAttribute("id", tableName +"Row"+ (last_row_number + 1));

    for (var count = 0; count < MAX_CELL_NUMBER ; count++) {
            var newCell = newRow.insertCell(count);
            newCell.setAttribute("id",TAG_ID_ELEMENTS[count] + (last_row_number+1));    
    }
    

}

create_newrow("expense");





