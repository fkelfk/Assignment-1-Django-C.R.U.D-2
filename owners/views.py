import json

from django.http import JsonResponse
from django.views import View

from .models import Owner, Dog

class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        ownerName = data['ownerName']
        ownerAge = data['ownerAge']
        ownerEmail = data['ownerEmail']

        owner = Owner.objects.create(
            name=ownerName,
            age=ownerAge,
            email=ownerEmail,

        )

        Dog.objects.create(
            name=data['name'],
            age=data['age'],
            owner=owner
        )

        return JsonResponse({'message': 'created'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        dogList = []

        for dog in dogs:
            dogList.append(
                {
                    "owner": dog.owner.name,
                    "dog_name": dog.name,
                    "dog_age": dog.age,
                }
            )

        return JsonResponse({'dogList': dogList}, status=200)


class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)

        Owner.objects.create(
            name=data['name'],
            age=data['age'],
            email=data['email'],
        )

        return JsonResponse({'message': 'created'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        ownerList = []
        for owner in owners:
            b = owner.dog_set.all()
            dogList = []
            for i in range(b.count()):
                c = b[i].name
                d = b[i].age
                e = [c, d]
                dogList.insert(i, e)
            ownerList.append(
                {
                    "name": owner.name,
                    "age": owner.age,
                    "email": owner.email,
                    "dog": f'{dogList}'
                }
            )

        return JsonResponse({'ownerList': ownerList}, status=200)