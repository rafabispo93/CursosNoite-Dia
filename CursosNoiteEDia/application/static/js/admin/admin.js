/*jslint plusplus: true, nomen: true*/
/*global G, L, $, Materialize, console, window */
$(function () {
    'use strict';
    function sendData(url, object) {
        $.ajax({
            url: url,
            type: 'POST',
            data: JSON.stringify(object),
            contentType: 'application/json',
            dataType: 'json',
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    }
    function submitCurso() {
        var inputs = $("#curso-form :input"), object = {}, count;
        for (count = 0; count < inputs.length; count++) {
            object[inputs[count].id] = inputs[count].value;
        }
        sendData('/adicionarCurso', object);
    }
    $("#register-curso").on('click', submitCurso);
});
