if ( window.history.replaceState ) {
  window.history.replaceState( null, null, window.location.href );
}

//Overlay 
function onSurface(id) {
  var element = document.getElementById(String(id));
  element.classList.remove("off-surface");
  element.classList.add("on-surface");  
}

function offSurface(id) {    
  var element = document.getElementById(String(id));
  element.classList.remove("off-surface");
  element.classList.add("off-surface");
}

function uniqueBudgetUrl(budgetID, id){    
    location.href="/budget/".concat('',budgetID);               
};





