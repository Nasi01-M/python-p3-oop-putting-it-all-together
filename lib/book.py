#!/usr/bin/env python3
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_pages(self):
        return self.pages

    def set_pages(self, pages):
        self.pages = pages

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price