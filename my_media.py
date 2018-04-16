import webbrowser

class MyMovie():
    def __init__(self, movie_title, movie_storyline, trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.trailer_youtube_url = trailer_youtube

    def movie_trailer(self):

        webbrowser.open(self.trailer_youtube_url)
