def get_response(user_text):
	if user_text.lower() in ['yes', 'yeah', 'ye', 'i loved it', 'i love it', 'i like it', 'i liked it',
	'i loved them', 'i love them', 'i like them', 'i liked them', 'great job', 'good job']:
		return 'Great to hear that! Stay tuned while I develop the ability to learn how to put forward more diverse films curated to you.'
	if user_text.lower() in ['no','nope', 'i didn\'t', 'i didn\'t like it']:
		return 'Sorry to hear that. Please leave feedback & stay tuned while I develop the ability to learn how to put forward more diverse films curated to you.'
	return 'Stay tuned while I develop the ability to talk to you.'
