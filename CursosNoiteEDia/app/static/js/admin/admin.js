$(function() {
  var submitCurso, getFormData;

  $("#register-curso").on('click', submitCurso.bind(this));

  function submitCurso (ev) {
    var inputs = $("#curso-form :input"), object = {};

    for (count = 0; count < inputs.length; count++) {
      object[inputs[count].id] = inputs[count].value;
    }
    sendData('/adicionarCurso', object);
  };
  function sendData (url, object) {
    $.ajax({
              url: url,
              data: object,
              type: 'POST',
              success: function(response) {
                  console.log(response);
              },
              error: function(error) {
                  console.log(error);
              }
    });
  }
});
