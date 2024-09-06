# SpringBoard_Flask_Boggle

## Halim's intervention

I added an index.js file that contains logic that would be executed in the home page

The logic I started with is listen to the submit event on the form submission and prevent it from
resubmitting. Instead of my console log, you would need to call the endpoint on the app.py server in order to validate your word, and react in the document accordingly.

I also added the app.py as it was missing from your submission, in this app.py what we do is
start a boggle game and send the board to the home.html to be rendered

Now what you need to do is correctly check the word from javascript's index js and react to the result.
