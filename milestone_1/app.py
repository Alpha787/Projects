MENU_PROMPT = "\nEnter 'a' to add a new movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie realease year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

def show_movies():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Realese year: {movie['year']}")


def find_movie():
    search_title = input("Enter movie title you're looking for:")

    for movie in movies:
        if movies["title"] == search_title:
            print_movie(movie)

user_options = {
    "a": add_movie,
    "l": show_movies,
    "f": find_movie
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()













