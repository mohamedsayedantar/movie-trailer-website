import webbrowser
# this class is used by movie_website_criation file


class Movie():
    def __init__(
     self, movie_title, movie_storyline, poster_image, trailar_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailar_youtube

    def show_trailar(self):
        webbrowser.open(self.trailer_youtube_url)
