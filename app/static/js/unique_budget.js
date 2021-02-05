var DEFAULT_ROW_HEIGHT = "2em";
var INCOME_NUMBER_ROW  = 0;
var EXPENSE_NUMBER_ROW  = 0;

// Expense table event Listener
var expenseTable = document.querySelector('#expenseTable');

expenseTable.addEventListener('click', function(event){
    var expenseCell = String(event.target.id);

    var editButton = document.getElementById("editButton");    
    if((editButton.value == 1) && (expenseCell.includes("expense_name") || expenseCell.includes("planned_amount"))){
        document.getElementById(expenseCell).setAttribute("contenteditable","true");
    }    
})

// Income table event Listener
var incomeTable = document.querySelector('#incomeTable');

incomeTable.addEventListener('click', function(event){
    var expenseCell = String(event.target.id);

    var editButton = document.getElementById("editButton");
    console.log(editButton.value);
    if((editButton.value == 1) && (expenseCell.includes("income_name") || expenseCell.includes("planned_amount"))){
        document.getElementById(expenseCell).setAttribute("contenteditable","true");
    }    
})


function create_newrow(tableName){
    var completeTableName = tableName+'Table'
    var MAX_CELL_NUMBER = 5;
    var TAG_ID_ELEMENTS = [tableName+"_name", tableName+"_planned_amount", tableName+"_actual_amount", tableName+"_difference"]
    var COUNT_ROWS_TABLE_ELEMENTS = document.getElementById(completeTableName).getElementsByTagName('tbody').length -1;
    var table = document.getElementById(completeTableName).getElementsByTagName('tbody')[COUNT_ROWS_TABLE_ELEMENTS];
    
    var last_row_number = table.rows.length;
    var newRow = table.insertRow(last_row_number);
    
    var row_id = tableName + "Row_"+ (last_row_number + 1);
    
    newRow.setAttribute("id", row_id);
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

        //Add remove button
        if(count === MAX_CELL_NUMBER-1){
            addRemoveButtonCell(newCell,row_id);
        }

    }
        
    if(completeTableName==="expenseTable"){
        EXPENSE_NUMBER_ROW++;
    }else{
        INCOME_NUMBER_ROW++;
    }
    
}

//Add remove button to Cell
function addRemoveButtonCell(cell, row_id){
    var iTag = document.createElement("i");                
    iTag.classList.add("fas","fa-trash-alt");
    var aTag = document.createElement("a");
    aTag.setAttribute("role","button");
    aTag.classList.add("btn", "btn-danger", "btn-sm");
    aTag.appendChild(iTag);
    cell.classList.add("remove-button-cell");
    cell.appendChild(aTag);
    cell.style.visibility = "visible";
    iTag.style.visibility = "visible";
    iTag.setAttribute("onclick","remove_row('"+ row_id +"')");
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
    var completeTableName = tableName+'Table'
    var COUNT_ROWS_TABLE_ELEMENTS = document.getElementById(completeTableName).getElementsByTagName('tbody').length -1;    
    var table = document.getElementById(completeTableName).getElementsByTagName('tbody')[COUNT_ROWS_TABLE_ELEMENTS];
    var last_row_number = table.rows.length - 1;
    
    //At the moment you cannot delete existing elements in the table    
    if(completeTableName==="expenseTable"){
        if(EXPENSE_NUMBER_ROW > 0){
            table.deleteRow(last_row_number)
            EXPENSE_NUMBER_ROW--;
        }else if(EXPENSE_NUMBER_ROW === 0){
            //I should ask to the user if he wants to eleminate 
            console.log("Modal to ask to delete an elemented in the database");
        }
    }else if(completeTableName==="incomeTable"){
        if(INCOME_NUMBER_ROW > 0){
            table.deleteRow(last_row_number)
            INCOME_NUMBER_ROW--;
        }else if(INCOME_NUMBER_ROW === 0){
            //I should ask to the user if he wants to eleminate 
            console.log("Modal to ask to delete an elemented in the database");
        }
    }
}


function remove_row(row_id){
    var row = document.getElementById(row_id);
    row.parentNode.removeChild(row);    
}


function toggle_button_visibility(){    
    var editButton = document.getElementById("editButton");
    //Ask for one, but affect both add and remove buttons
    var expenseAddButton = document.getElementById('expenseAddButton');    
    var incomeAddButton = document.getElementById('incomeAddButton');    
    
    var SaveButton = document.getElementById('SaveButton');    
    var CancelButton = document.getElementById('CancelButton');    

    if(editButton.value != 1){                
        expenseAddButton.style.display = "block";
        incomeAddButton.style.display = "block";
        toggle_remove_buttons_visibility();

        editButton.classList.add("btn-secondary");
        editButton.classList.remove("btn-success");        
        editButton.value = 1;

        SaveButton.style.display = "block";        
        CancelButton.style.display = "block";        
    } else {         
        expenseAddButton.style.display = "none";
        incomeAddButton.style.display = "none";        
        toggle_remove_buttons_visibility();

        editButton.classList.remove("btn-secondary");
        editButton.classList.add("btn-success");
        editButton.value = 0;       

        SaveButton.style.display = "none";        
        CancelButton.style.display = "none";                
        location.reload()
    }        
    
}

function toggle_remove_buttons_visibility(){
    var removebutton = document.getElementsByClassName("remove-button-cell");

    for(var count = 0; count < removebutton.length; count++){            
        if(editButton.value != 1){        
            removebutton[count].style.visibility="visible";
        } else {
            removebutton[count].style.visibility="hidden";
        }
    }
}

//Capture event Save Button 
document.querySelector('#SaveButton').addEventListener('click', function(event){    
    var formData = new FormData();

    var xhttp = new XMLHttpRequest();
    var currentURL = window.location.href.split("/");

    var expenseItems = getTableValuesIntoJson("expenseTable");
    var incomeItems = getTableValuesIntoJson("incomeTable");        
    
    formData.append("budget_id",currentURL[4]);
    formData.append("income",incomeItems);
    formData.append("expense",expenseItems);

    xhttp.open("POST", "/update_income_expenses", true);
    xhttp.send(formData);    
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200){
            alert("Saved");
        }
        console.log(this.readyState);
    };    
    toggle_button_visibility();    
});


//Capture event Cancel Button 
document.querySelector('#CancelButton').addEventListener('click', function(event){    
    //I prefer to reload the page instead of resenting the states of every element.
    location.reload();          
})


function getTableValuesIntoJson(tableName){
    table = document.getElementById(tableName);
    var items = [];    

    for (var count = 2, row; row = table.rows[count]; count++){   
        var rowElements = {"name":"", "planned_amount":0.0, "actual_amount":0.0};               
        rowElements["name"]= row.cells[0].innerHTML.replace(/&nbsp;/g,' ');        
        rowElements["planned_amount"]= row.cells[1].innerHTML.replace(/&nbsp;/g,' ');
        rowElements["actual_amount"]= row.cells[2].innerHTML.replace(/&nbsp;/g,' ');                

        if(rowElements["planned_amount"] === ""){
            rowElements["planned_amount"] = "0.0";
            console.log(rowElements["planned_amount"]);
        }
        
        if(rowElements["actual_amount"] === ""){
            rowElements["actual_amount"] = "0.0";
            console.log(rowElements["actual_amount"]);
        }
        if(rowElements["name"] !== "")
        items.push(rowElements);
    }

    if (tableName === "incomeTable"){
        var alltableElements = {"incomeItems":[]};
        alltableElements["incomeItems"] = items;        
    }else {
        var alltableElements = {"expenseItems":[]};
        alltableElements["expenseItems"] = items;        
    }        
    return JSON.stringify(alltableElements);
}