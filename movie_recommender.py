"""1. encode genres -> 2.add_new_user -> 3.find_similar_users -> 4.recommend_movies """

import pandas as pd 
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse
import numpy as np

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

ratings = ratings.fillna(0)

genre_list = ['Fantasy', 'Film-Noir', 'Mystery', 'Documentary', 'Animation',
       'Comedy', 'Western', 'War', 'Crime', 'Horror', 'Children', 'Musical',
       'Thriller', 'Action', 'IMAX', 'Adventure', 'Drama', 'Sci-Fi']

def encode_genres():
	user_genres = pd.DataFrame(index=ratings['userId'].unique(), columns=genre_list)
	for genre in genre_list:
		#find all movies that fall in that genre
		film_list = movies[movies['genres'].str.contains(genre)]['movieId']
		#find how a user rates movies of that genre on average
		grpby = ratings[ratings['movieId'].isin(film_list)].groupby(['userId'])['rating'].mean()
		#set the genres columns row to the user's corresponding avgs
		user_genres[genre] = grpby
	return user_genres


def add_new_user(genre_preferences, user_genres):
	#genre preferences is a dict that contains the user's indicated preferences
	return user_genres.append(genre_preferences,ignore_index=True)


def find_similar_users(user_genres):
	#returns 50 most similar user IDs
	user_genres=user_genres.fillna(0)
	df1 = cosine_similarity(user_genres)
	#print(df1)
	sim = pd.DataFrame(data=df1, index=user_genres.index, columns=user_genres.index)
	last_user = sim.tail(1).index
	sim_users = sim[last_user].nlargest(50,last_user).index#[611]
	#print(sim_users)
	return sim_users


def find_movies(sim_users):
	rec_movies = ratings[ratings['userId'].isin(sim_users)].groupby(['movieId'])['rating'].mean().sort_values(ascending=False)
	top_rec_movies = rec_movies[:10]
	#print(movies[movies['movieId'].isin(top_rec_movies.index)])
	return movies[movies['movieId'].isin(top_rec_movies.index)]['title']


def recommend_movies(genre_preferences):
	user_genres = encode_genres()
	user_genres = add_new_user(genre_preferences, user_genres)
	sim_users = find_similar_users(user_genres)
	rec_movies = find_movies(sim_users)
	return rec_movies

