from django.shortcuts import render
from django.views.generic import ListView

from books.models import Publisher, Author, Book


class PublisherListView(ListView):
	model = Publisher