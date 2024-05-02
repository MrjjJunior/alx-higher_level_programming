#!/usr/bin/env node 

$(document).ready(function() {
  $("#toggle_header").click(function() {
    $("header").toggleClass("red green");
  });
});

