var DEFAULT_ROW_HEIGHT = "2em";
var GLOBAL_NUMBER_ROW  = 0;

function create_newrow(tableName){

    var MAX_CELL_NUMBER = 4;
    var TAG_ID_ELEMENTS = [tableName+"_name", tableName+"_planned_amount", tableName+"_actual_amount", tableName+"_difference"]
    var COUNT_ROWS_TABLE_ELEMENTS = document.getElementById(tableName+'Table').getElementsByTagName('tbody').length -1;

    var table = document.getElementById(tableName+'Table').getElementsByTagName('tbody')[COUNT_ROWS_TABLE_ELEMENTS];
    var last_row_number = table.rows.length;
    var newRow = table.insertRow(last_row_number);
    newRow.setAttribute("id", tableName +"Row"+ (last_row_number + 1));
    newRow.style.height = DEFAULT_ROW_HEIGHT;

    for (var count = 0; count < MAX_CELL_NUMBER ; count++) {
            var newCell = newRow.insertCell(count);
            newCell.setAttribute("id",TAG_ID_ELEMENTS[count] + (last_row_number+1));    
    }
    GLOBAL_NUMBER_ROW++;
    
}

function remove_lastrow(tableName){
    var COUNT_ROWS_TABLE_ELEMENTS = document.getElementById(tableName+'Table').getElementsByTagName('tbody').length -1;
    var table = document.getElementById(tableName+'Table').getElementsByTagName('tbody')[COUNT_ROWS_TABLE_ELEMENTS];
    var last_row_number = table.rows.length - 1;
    //At the moment you cannot delete existing elements in the table
    if(GLOBAL_NUMBER_ROW>0){
        table.deleteRow(last_row_number)
        GLOBAL_NUMBER_ROW--;
    }else if(GLOBAL_NUMBER_ROW === 0){
        //I should ask to the user if he wants to eleminate 
        console.log("Modal to ask to delete an elemented in the database");
    }
}



