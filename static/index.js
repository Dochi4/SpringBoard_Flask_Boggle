$(document).ready(function () {
  $("#boggleForm").submit(function (e) {
    e.preventDefault();
    let word = $("#word").val();

    $.ajax({
      url: '/check-word',
      method: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({ word: word }),
      success: function (response) {
        $("#result").text(`Result: ${response.result}`);

        $.ajax({
          url: '/update-score',
          method: 'POST',
          contentType: 'application/json',
          data: JSON.stringify({ result: response.result }),
          success: function (scoreResponse) {
            $("#score").text(scoreResponse.score);
          },

        });
      }
    });
  })


  let counter = 60;
  setInterval(function () {
    counter--;

    if (counter <= 0) {
      $('#time').html("Stop Playing - 0");
      $("#boggleForm").find("input, button").prop("disabled", true);
      return;
    } else {
      $('#time').text(counter);
    }
  }, 1000);

})

