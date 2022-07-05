import json

from django.http import JsonResponse
from django.views import View

from .models import Movies, Actor


class MovieView(View):
    def get(self, request):
        movies = Movies.objects.all()
        movieList = []

        for movie in movies:
            b = movie.actors.all()
            actorList = []
            for i in range(b.count()):
                c = b[i].first_name
                actorList.insert(i, c)
            movieList.append(
                {

                    "title": movie.title,
                    "release_date": movie.release_date,
                    "running_time": movie.running_time,
                    "actor": f'{actorList}',
                }

            )

        return JsonResponse({'movieList': movieList}, status=200)

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        actorList = []

        for actor in actors:
            b = actor.movies_set.all()
            movieList = []
            for i in range(b.count()):
                c = b[i].title
                movieList.insert(i, c)
            actorList.append(
                {
                    "first_name": actor.first_name,
                    "last_name": actor.last_name,
                    "date_of_birth": actor.date_of_birth,
                    "movies": f'{movieList}',

                }
            )
        return JsonResponse({'actorList': actorList}, status=200)
