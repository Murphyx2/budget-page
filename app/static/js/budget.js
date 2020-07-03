$('#newBudget').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var recipient = button.data('title') // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this)
  modal.find('.modal-title').text('Create new' + recipient)
  modal.find('.modal-body input').val(recipient)
})

if ( window.history.replaceState ) {
  window.history.replaceState( null, null, window.location.href );
}

function onSurface(id) {
  document.getElementById(id).setAttribute("style","background: #F0F8FF;");  
}

function offSurface(id) {  
  document.getElementById(id).setAttribute("style","background: white;");
}

function uniqueBudgetUrl(budgetID, id){
  $('#'.concat('',id)).click(function(e){
    if($(e.target).is('#dropdown0')){
      //e.preventDefault();
      return;
    }else{
      location.href="/budget/".concat('',budgetID);         
    }     
  });
};


