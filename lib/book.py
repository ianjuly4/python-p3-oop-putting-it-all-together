#!/usr/bin/env python3

class Book:
   def __init__(self, title, page_count):
      self._title = title
      self._page_count = page_count
   
   @property
   def title(self):
      """The title property"""
      return self._title
   @property
   def page_count(self):
      """The page_count property"""
      return self._page_count
   
   @title.setter
   def title(self, title):
      self._title = title

   @page_count.setter
   def page_count(self, page_count):
      """page_count must be an integer"""
      if type(page_count) == (int):
         self._page_count = page_count
      else:
         print("page_count must be an integer")

   def turn_page(self):
      print("Flipping the page...wow, you read fast!")


book  = Book("Great Gatsby", 277)
book._title
book._page_count
book.turn_page