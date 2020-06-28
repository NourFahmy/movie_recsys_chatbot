from flask import Flask, render_template, request
from os import path
import requests
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
#from chatterbot.trainers import ListTrainer
from bot import get_response
from movie_recommender import recommend_movies
#https://mc.ai/how-create-chatbot-in-few-minutes-using-python-or-flask/

app = Flask(__name__, static_url_path='/static')
basepath = path.dirname(__file__)
"""
bot = ChatBot("Python-BOT")
trainer = ListTrainer(bot)
trainer.train(['what is your name?', 'My name is Python-BOT'])
trainer.train(['who are you?', 'I am a BOT'])
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
"""
user_ratings = {}

@app.route("/")
def index():    
    return render_template("index.html") 

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(get_response(userText)) 

@app.route('/user_preferences', methods=['POST'])
def get_user_preferences():
	user_preferences = {}
	for genre in ['Fantasy', 'Film-Noir', 'Mystery', 'Documentary', 'Animation',
       'Comedy', 'Western', 'War', 'Crime', 'Horror', 'Children', 'Musical',
       'Thriller', 'Action', 'IMAX', 'Adventure', 'Drama', 'Sci-Fi']:
		user_preferences[genre] = request.form.get(genre)
	#print(user_preferences)
	print(recommend_movies(user_preferences))
	return render_template("index.html") 


def update_user_preference(key, value):
	user_ratings[key] = value
	print(user_ratings)

if __name__ == "__main__":    
    app.run(host="0.0.0.0", port=5005, debug=True)