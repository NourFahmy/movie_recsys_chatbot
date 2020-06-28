#from app import update_user_preferences

def get_response(user_text):
	if user_text == 'yes':
		return 'how would you rate comedy out of 5? Please type your answer as follows: Comedy (then the number out of 5)'
	if type(user_text) == int:
		return 'recorded your preference'
	if 'Comedy' in user_text:
		#update_user_preferences('Comedy', int(user_text[-1]))
		return 'How would you rate comedy out of 5? Please type your answer as follows: Drama (then the number out of 5)'
	return 'great'