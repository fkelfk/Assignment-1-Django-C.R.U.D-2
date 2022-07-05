import json

from django.http import JsonResponse
from django.views import View

from .models import Movies, Actor


class MovieView(View):
    def get(self, request):
        movies = Movies.objects.all()

        movieList = []

        for movie in movies:
             movieList.append(
                {
                    "actor": movie.actors.name,
                    "title": movie.title,
                    "release_date": movie.release_date,
                    "running_time": movie.running_time,
                }
            )

        return JsonResponse({'movieList': movieList}, status=200)

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        actorList = []

        for actor in actors:
             actorList.append(
                {
                    "first_name": actor.first_name,
                    "last_name": actor.last_name,
                    "date_of_birth": actor.date_of_birth,
                    # "movie": actor.movies.title
                }
            )
        return JsonResponse({'actorList': actorList}, status=200)
