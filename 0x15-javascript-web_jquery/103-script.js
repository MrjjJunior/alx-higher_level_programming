#!/usr/bin/node
$(document).ready(function() {
    function fetchTranslation() {
      const langCode = $('#language_code').val();
      $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, function(data) {
        $('#hello').text(data.hello);
      });
    }
  
    $('#btn_translate').click(function() {
      fetchTranslation();
    });
  
    $('#language_code').keypress(function(event) {
      if (event.which === 13) { // 13 is the Enter key
        fetchTranslation();
        event.preventDefault(); // Prevent the default action of the Enter key
      }
    });
  });  