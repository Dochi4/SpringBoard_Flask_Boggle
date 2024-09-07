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
          success: function (scoreResp) {
            $("#score").text(scoreResp.score);
          },

        });
      }
    });
  })


  let counter = 60;
  const timer = setInterval(function () {
    counter--;

    if (counter <= 0) {
      $('#time').html("Stop Playing - 0");
      $("#boggleForm").find("input, button").prop("disabled", true);
      clearInterval(timer);
      endGame();
      return;
    } else {
      $('#time').text(counter);
    }
  }, 1000);


  function endGame() {
    const score = parseInt($("#score").text());
    $.ajax({
      url: '/post-score',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({ score: score }),
      success: function (response) {
        $('#highscore').text(response.highscore);
        $('#nplays').text(response.nplays);
      },
      error: function () {
        console.error('Error posting score.');
      }
    });
  }

})



