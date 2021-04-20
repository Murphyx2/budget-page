//select from budget list
function transactionPage(budgetID, id){    
    location.href="/transactions/".concat('',budgetID);
};

let selectBudget = document.querySelector('#budget_list');

//Event for changing budget selected.
selectBudget.addEventListener('change', (event) => {    
    window.location.href="/transactions/".concat('',selectBudget.value);    
});





