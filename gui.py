from appJar import gui
import numpy as np
import dataprocess


movie_entry = "Movies:"
search_btn = "search_btn"
message_lbl = "message_lbl"
app = gui("Recommendation System")
movie_list = np.array([])


def getMoviesText(movies):
	msg = ""
	for i in range(0, len(movies)):
		msg = msg + movies[i] + "\n"
	return msg
	


def getEntry(btn):
	movie = app.getEntry(movie_entry)
	if movie in movie_list:
		app.setMessage(message_lbl, getMoviesText(dataprocess.find(movie)))
	else:
		app.setMessage(message_lbl, "This movie isn't in our database")
	print movie


def main():
	global movie_list
	movie_list = np.append(movie_list,dataprocess.get_movies())
	startGUI()

def startGUI():
	#Basic GUI Configuration
	app.setGeometry("500x400")
	app.setLocation("CENTER")

	#Labels Configuration
	app.addLabelAutoEntry(movie_entry, movie_list)
	app.setEntryDefault(movie_entry, "Enter a movie here...")

	#Button Configuration
	app.addNamedButton("Search", search_btn, getEntry)

	#Message Configuration
	app.addEmptyMessage(message_lbl)

	app.go()


if __name__ == '__main__':
	main()
