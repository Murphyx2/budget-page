//select from budget list
function transactionPage(budgetID, id){    
    location.href="/transactions/".concat('',budgetID);
};

let selectBudget = document.querySelector('#budget_list');

//Event for changing budget selected.
selectBudget.addEventListener('change', (event) => {    
    let expenseTransaction = document.getElementById("expenseIframe");
    let incomeTransaction = document.getElementById("incomeIframe");
    expenseTransaction.src = "/expenseTransaction/".concat('',selectBudget.value);
    incomeTransaction.src = "/incomeTransaction/".concat('',selectBudget.value);

});


