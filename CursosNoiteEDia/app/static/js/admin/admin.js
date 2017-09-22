var submitCurso, getFormData;

submitCurso = function (ev) {
  console.log(getFormData('#cursos-form'));
  window.alert("jkabd");

}();

getFormData = function (dom_query) {
   var i, record, out = {}, s_data = $(dom_query).serializeArray();
   for (i = 0; i < s_data.length; i++) {
       record = s_data[i];
       out[record.name] = record.value;
   }
   return out;
}
