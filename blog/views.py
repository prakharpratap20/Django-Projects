from django.shortcuts import render
from datetime import date

posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountain.jpg",
        "author": "Prakhar",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        

    }
]

# Create your views here.


def starting_page(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
