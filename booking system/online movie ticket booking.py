#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#//front end//
import tkinter as tk
from tkinter import messagebox

class MovieTicketBookingSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Movie Ticket Booking System")
        self.master.geometry("400x300")

        self.movie_options = ["Avengers: Endgame", "The Lion King", "Joker", "Frozen 2"]
        self.selected_movie = tk.StringVar(master)
        self.selected_movie.set(self.movie_options[0])

        self.label_movie = tk.Label(master, text="Select Movie:")
        self.label_movie.pack()

        self.movie_menu = tk.OptionMenu(master, self.selected_movie, *self.movie_options)
        self.movie_menu.pack()

        self.label_tickets = tk.Label(master, text="Number of Tickets:")
        self.label_tickets.pack()

        self.num_tickets = tk.Entry(master)
        self.num_tickets.pack()

        self.book_button = tk.Button(master, text="Book Tickets", command=self.book_tickets)
        self.book_button.pack()

    def book_tickets(self):
        movie = self.selected_movie.get()
        num_tickets = self.num_tickets.get()

        if not num_tickets.isdigit():
            messagebox.showerror("Error", "Please enter a valid number of tickets.")
            return

        num_tickets = int(num_tickets)

        # Here you would implement the logic to book the tickets,
        # such as checking availability, updating database, etc.
        # For now, we'll just display a message.
        messagebox.showinfo("Success", f"Tickets booked for {movie} ({num_tickets} tickets).")

def main():
    root = tk.Tk()
    app = MovieTicketBookingSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()


# In[6]:


#//back end//
class Movie:
    def __init__(self, title, genre, rating, duration):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.duration = duration

class BookingSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def search_movie_by_title(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        return None

    def search_movie_by_genre(self, genre):
        found_movies = []
        for movie in self.movies:
            if movie.genre.lower() == genre.lower():
                found_movies.append(movie)
        return found_movies

# Example usage:
booking_system = BookingSystem()

movie1 = Movie("Inception", "Sci-Fi", "PG-13", 150)
movie2 = Movie("The Shawshank Redemption", "Drama", "R", 142)
movie3 = Movie("The Dark Knight", "Action", "PG-13", 152)

booking_system.add_movie(movie1)
booking_system.add_movie(movie2)
booking_system.add_movie(movie3)

# Searching for a movie by title
searched_movie = booking_system.search_movie_by_title("Inception")
if searched_movie:
    print("Found:", searched_movie.title)
else:
    print("Movie not found")

# Searching for movies by genre
searched_movies = booking_system.search_movie_by_genre("Action")
if searched_movies:
    print("Found", len(searched_movies), "movies in Action genre:")
    for movie in searched_movies:
        print(movie.title)
else:
    print("No movies found in the Action genre")


# In[ ]:




