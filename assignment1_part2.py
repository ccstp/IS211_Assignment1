# ASSIGNMENT 1_PART 02

# !/usr/bin/env python
# -*- coding: utf-8 -*-


class Book:
    """
    Class used to represent a Book

    Attributes:
    author (str): The name of the author
    title (str): The title of the book
    """
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        """
        This function prints out a formatting string displaying the book's title and author.
        """
        print(f'{self.title}, written by {self.author}')


if __name__ == "__main__":
    book_one = Book("John Steinbeck", "Of Mice and Men")
    book_two = Book("Harper Lee", "To Kill a Mockingbird")
    book_one.display()
    book_two.display()