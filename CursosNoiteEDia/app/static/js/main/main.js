var listenClick;

listenClick = function () {
  var options = {
          "backdrop" : "static",
          "show":true
      };
  $(".cursos-item").on("click", function(){
      $('#basicModal').modal(options);
  });
}();
