from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def setUp(self):
           
        self.client = app.test_client()
        app.config['TESTING'] = True
            
    def test_homepage(self):
       
        with self.client:
            response = self.client.get('/')

            with self.client.session_transaction() as sess:
                self.assertIn('current_board', sess)
                self.assertIsNone(sess.get('highscore'))
                self.assertIsNone(sess.get('nplays'))

            self.assertIn(b'<p>High Score:', response.data)
            self.assertIn(b'Score:', response.data)
            
        
    def test_valid_word(self):
        with self.client.session_transaction() as sess:
            sess['current_board'] = [["C", "A", "T", "T", "T"], 
                                     ["C", "A", "T", "T", "T"], 
                                     ["C", "A", "T", "T", "T"], 
                                     ["C", "A", "T", "T", "T"], 
                                     ["C", "A", "T", "T", "T"]]

        response = self.client.post('/check-word', json={'word': 'cat'})
        self.assertEqual(response.json['result'], 'ok')  

    def test_update_score(self):
        with self.client.session_transaction() as sess:
            sess['score'] = 5
                            
    def test_post_score(self):
        with self.client:
            response = self.client.post('/post-score', json={'score': 10})
            self.assertEqual(response.json['highscore'], 10)
            self.assertEqual(response.json['nplays'], 1)