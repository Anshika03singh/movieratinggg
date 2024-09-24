class Movie:
    """
    Class to represent a Movie object.
    Each movie has a title and a list of ratings.
    """
    def __init__(self, title):
        self.title = title
        self.ratings = []

    def add_rating(self, rating):
        """
        Adds a rating to the movie.
        Rating should be between 1 and 5.
        """
        if 1 <= rating <= 5:
            self.ratings.append(rating)
            print(f"Rating {rating} added to '{self.title}'")
        else:
            print("Invalid rating. Please enter a rating between 1 and 5.")

    def average_rating(self):
        """
        Calculates and returns the average rating of the movie.
        Returns 0 if there are no ratings.
        """
        if self.ratings:
            return sum(self.ratings) / len(self.ratings)
        return 0

    def __str__(self):
        """
        Returns a string representation of the movie with its average rating.
        """
        avg_rating = self.average_rating()
        return f"{self.title}: {avg_rating:.1f} stars"


class MovieRatingSystem:
    """
    Class to represent a Movie Rating System.
    It stores a list of movies and provides functionalities
    like adding movies, rating them, and displaying top-rated movies.
    """
    def __init__(self):
        self.movies = []

    def add_movie(self, title):
        """
        Adds a new movie to the system.
        """
        movie = Movie(title)
        self.movies.append(movie)
        print(f"Movie '{title}' added to the system.")

    def rate_movie(self, title, rating):
        """
        Rates an existing movie by its title.
        """
        for movie in self.movies:
            if movie.title == title:
                movie.add_rating(rating)
                return
        print(f"Movie '{title}' not found in the system.")

    def display_movies(self):
        """
        Displays all movies with their average ratings.
        """
        if not self.movies:
            print("No movies in the system yet.")
        else:
            print("Movies in the system:")
            for movie in self.movies:
                print(movie)

    def top_movies(self):
        """
        Displays movies sorted by their average rating in descending order.
        """
        if not self.movies:
            print("No movies available to display.")
            return
        
        sorted_movies = sorted(self.movies, key=lambda movie: movie.average_rating(), reverse=True)
        print("Top rated movies:")
        for movie in sorted_movies:
            print(movie)


if __name__ == "__main__":
    # Instantiate the Movie Rating System
    system = MovieRatingSystem()

    # Adding movies
    system.add_movie("Inception")
    system.add_movie("Interstellar")
    system.add_movie("3 idiots")
    system.add_movie("The Matrix")

    # Rating movies
    system.rate_movie("Inception", 5)
    system.rate_movie("Inception", 4)
    system.rate_movie("Interstellar", 5)
    system.rate_movie("3 idiots", 4)
    system.rate_movie("The Matrix", 3)

    # Display all movies with their ratings
    print("\nAll Movies:")
    system.display_movies()

    # Display top-rated movies
    print("\nTop Rated Movies:")
    system.top_movies()
