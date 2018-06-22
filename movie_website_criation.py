import media
import fresh_tomatoes

"""
this file generate new movies by calling the class movie
from media file and give this class the name of the movie
and a youtube trailer for it and a photo url and small
description of the movie and giving all of this data back to
fresh fresh_tomatoes file to generate th web page.
"""

zootopia = media.Movie(
    "zootopia", "anime movie with rabbit and a fox",
    "https://i.ytimg.com/vi/d4WEUn0yS74/movieposter.jpg",
    "https://www.youtube.com/watch?v=jWM0ct-OLsM"
    )

godzilla_2014 = media.Movie(
    "Godzilla 2014",
    "a strange animal defend the earth",
    "https://i.ytimg.com/vi/l_skUvZMBys/maxresdefault.jpg",
    "https://www.youtube.com/watch?v=-ieuv_84nmc"
    )

man_of_steel = media.Movie(
    "Man Of Steel",
    "strong type of humans send them last child to the earth",
    """https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOCMc3EZsIZFAV930p
    -YZpmczTuXDp2VhGI-bf8QCYj-Gc5usENQ""",
    "https://www.youtube.com/watch?v=T6DJcgm3wNY"
    )

the_avengers = media.Movie(
    "The Avengers",
    "group of heroes save the humanity",
    """https://encrypted-tbn0.gstatic.com/image
    s?q=tbn:ANd9GcRBGyNLTAdU1W8Kxrejo1Xhf8OqAyi3l7Wfa_nk_9fBdbyHo8n-""",
    "https://www.youtube.com/watch?v=eOrNdBpGMv8"
    )

The_November_Man = media.Movie(
    "The November Man",
    """An ex-CIA operative is brought back in on a very personal mission
    and finds himself pitted against his former pupil""",
    "https://i.ytimg.com/vi/lfDP9jMoWgM/maxresdefault.jpg",
    "https://www.youtube.com/watch?v=jREIRTyj9Mk"
    )

lucy = media.Movie(
    "lucy",
    """she find herself able to move objects with her mind, and cannot feel
    pain and other discomforts""",
    """https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlwBBTv2dlAo
    7k93AXeGqeDTrf0E8tEcnoOq9XiuZN9CgIGYz2""",
    "https://www.youtube.com/watch?v=MVt32qoyhi0"
    )

movies = [
    zootopia, godzilla_2014, man_of_steel, the_avengers,
    The_November_Man, lucy
    ]
fresh_tomatoes.open_movies_page(movies)
