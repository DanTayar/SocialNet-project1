from flask import Flask
from flask import render_template
app = Flask(__name__)

from profiles import profiles, find_profile
from statuses import statuses


@app.route("/")
def index():
	return render_template('index.html', profiles=profiles)


@app.route("/profiles/<username>")
def profile(username):
	#process the data
	profile = find_profile(username)
	statuses_list = []
	for i in statuses:
		if i ['user_id'] == profile['id']:
			statuses_list.append(i)
	return render_template('profile.html', profile=profile ,statuses=statuses_list)

@app.route("/profiles/<username>/friends")
def friends(username):
	profile = find_profile(username)
	friends_list = []
	for friend_id in profile['friends']:
		for friend_profile in profiles:
			if friend_id  ==  friend_profile['id']:
					friends_list.append(friend_profile)

	return render_template('friends.html', profile=profile , friends=friends_list)


