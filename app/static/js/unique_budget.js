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
            newCell.setAttribute("id",TAG_ID_ELEMENTS[count] + (last_row_number + 1));
            
            //You can only edit the name or the planned amount
            if(TAG_ID_ELEMENTS[count] === TAG_ID_ELEMENTS[0]){
                newCell.setAttribute("contenteditable","true");

            }else if(TAG_ID_ELEMENTS[count] === TAG_ID_ELEMENTS[1]){
                newCell.setAttribute("contenteditable","true");
                newCell.setAttribute("onkeypress", 'return isNumberKey(event)');                
            }
    }
    GLOBAL_NUMBER_ROW++;
    
}

//Allow only numbers
function isNumberKey(event){
    var charCode = (event.which) ? event.which : event.keyCode
    if (charCode > 31 && (charCode != 46 &&(charCode < 48 || charCode > 57))){
        return false;
    }
    return true;
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


function toggle_button_visibility(){    
    var editButton = document.getElementById("editButton");
    //Ask for one, but affect both add and remove buttons
    var expenseAddButton = document.getElementById('expenseAddButton');
    var expenseRemoveButton = document.getElementById('expenseRemoveButton');
    var incomeAddButton = document.getElementById('incomeAddButton');
    var incomeRemoveButton = document.getElementById('incomeRemoveButton');
    
    var incomeSaveButton = document.getElementById('incomeSaveButton');
    var expenseSaveButton = document.getElementById('expenseSaveButton');
    var incomeCancelButton = document.getElementById('incomeCancelButton');
    var expenseCancelButton = document.getElementById('expenseCancelButton');

    if(editButton.value != 1){        
        expenseRemoveButton.style.display = "block";
        incomeRemoveButton.style.display = "block";
        expenseAddButton.style.display = "block";
        incomeAddButton.style.display = "block";

        editButton.classList.add("btn-secondary");
        editButton.classList.remove("btn-success");
        editButton.value = 1;

        incomeSaveButton.style.display = "block";
        expenseSaveButton.style.display = "block";
        incomeCancelButton.style.display = "block";
        expenseCancelButton.style.display = "block";
    } else { 
        expenseRemoveButton.style.display = "none";
        incomeRemoveButton.style.display = "none";
        expenseAddButton.style.display = "none";
        incomeAddButton.style.display = "none";
        editButton.classList.remove("btn-secondary");
        editButton.classList.add("btn-success");
        editButton.value = 0;

        incomeSaveButton.style.display = "none";
        expenseSaveButton.style.display = "none";
        incomeCancelButton.style.display = "none";
        expenseCancelButton.style.display = "none";
    }    

}

function testing(){
    console.log('I did something')
}


