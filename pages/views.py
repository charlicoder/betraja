from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class GreetingView(View):
	greetings = "Good Day"

	def get(self, request):
		return HttpResponse(self.greetings)

