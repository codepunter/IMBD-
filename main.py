# importing the module
import imdb
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # creating instance of IMDb
    ia = imdb.IMDb()

    # getting top 250 movies
    top250_movie = ia.get_top250_movies()
    # printing only first 10 movies title
    movie_df = pd.DataFrame(columns=['movie_id', 'movie_name', 'rating', 'votes'])

    for movie_count in range(250):
        movie_id = top250_movie[movie_count].movieID
        movie_obj = ia.get_movie(movie_id)
        movie_df.loc[len(movie_df)] = [movie_id, movie_obj.data['title'], movie_obj.data['rating'],
                                       movie_obj.data['votes']]

    movie_df.to_csv("Output.csv")


def createscattergraph(filename="Output.csv"):
    movie_df = pd.read_csv(filename)
    plt.scatter(movie_df['rating'].tolist(), movie_df['votes'].tolist(), c="blue")
    plt.xlabel("Ratings")
    plt.ylabel("Votes")
    # To show the plot
    # plt.show()
    plt.savefig('scatterplot.jpg', bbox_inches='tight', dpi=150)


if __name__ == "__main__":
    createscattergraph()