document.addEventListener('DOMContentLoaded', function () {
    var alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function(alert) {
      setTimeout(function() {
        alert.classList.remove('show');
        alert.classList.add('hide'); 
        alert.remove(); 
      }, 3000);
    });
});
