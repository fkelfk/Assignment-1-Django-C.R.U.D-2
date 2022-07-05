import json

from django.http import JsonResponse
from django.views import View

from .models import Movies, Actor


class MovieView(View):
    def get(self, request):
        movies = Movies.objects.all()
        movieList = []


        for movie in movies:
            m1 = movie.actors.all()
            movieList.append(
                {
                    "actor": f'{[i for i in m1]}',
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
                    "movies": f'{actor.movies_set.all()}',
                    "first_name": actor.first_name,
                    "last_name": actor.last_name,
                    "date_of_birth": actor.date_of_birth,

                }
            )
        return JsonResponse({'actorList': actorList}, status=200)
