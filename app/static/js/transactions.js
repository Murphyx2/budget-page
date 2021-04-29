//select from budget list
function transactionPage(budgetID, id){    
    location.href="/transactions/".concat('',budgetID);
};

let selectBudget = document.querySelector('#budget_list');

//Event for changing budget selected.
selectBudget.addEventListener('change', (event) => {    
    window.location.href="/transactions/".concat('',selectBudget.value);    
});

let expense_transaction_table_space = document.querySelector('#expense_transaction_table_space')
let expense_transaction_edit_bar = document.querySelector('#expense_transaction_edit_bar');
let income_transaction_edit_bar = document.querySelector('#income_transaction_edit_bar');

document.querySelectorAll('.table-space').forEach(element => {
    element.addEventListener('click', event =>{
        expense_transaction_edit_bar.style.display = "block";
        income_transaction_edit_bar.style.display = "block";
        //Make tables editable    
        let table_rows_income_length = document.getElementById("income_table").rows.length;
        set_expense_table_content_editable();
    });
});

/*expense_transaction_table_space.addEventListener('dblclick',(event) =>{    
    expense_transaction_edit_bar.style.display = "block";
    income_transaction_edit_bar.style.display = "block";
    //Make tables editable    
    let table_rows_income_length = document.getElementById("income_table").rows.length;
    set_expense_table_content_editable();

});*/

function set_expense_table_content_editable(){
    let table_rows_expense_length = document.getElementById("expense_table").rows.length;

    for(count = 0; count < table_rows_expense_length-1; count++){        
        let expenses_transaction_date = document.getElementById("expenses_transaction_date_"+count);
        let expenses_transaction_amount = document.getElementById("expenses_transaction_amount_"+count);
        let expenses_transaction_description = document.getElementById("expenses_transaction_description_"+count);
        let expenses_transaction_category = document.getElementById("expenses_transaction_category_"+count);

        expenses_transaction_date.setAttribute("contenteditable", "true");
        expenses_transaction_amount.setAttribute("contenteditable", "true");
        expenses_transaction_description.setAttribute("contenteditable", "true");
        expenses_transaction_category.setAttribute("contenteditable", "true");
    }
}


//This won't work unless the section is content editable
expense_transaction_table_space.addEventListener('keyup', (event) => {
    if(event.keyCode == 13){
        event.preventDefault();    
        console.log('User press enter');        
    }    
});

//Expense buttons fuctions
let add_expense_transaction = document.querySelector('#add_expense_transaction');
let cancel_expense_transaction = document.querySelector('#cancel_expense_transaction');

cancel_expense_transaction.addEventListener('click', (event)=> {
    expense_transaction_edit_bar.style.display = "None";
    income_transaction_edit_bar.style.display = "None";
});