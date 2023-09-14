from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountain.jpeg",
        "author": "Prakhar",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking Adventure",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Mountain hiking is a thrilling adventure that everyone should experience at least once in their life. The breathtaking views and the sense of accomplishment when you reach the summit are unmatched. In this post, I'll take you on a journey to the mountains, share my experiences, and provide some tips for an enjoyable hiking adventure. So, fasten your hiking boots, and let's explore the beauty of the great outdoors!
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.avif",
        "author": "Prakhar",
        "date": date(2022, 3, 10),
        "title": "The Joy of Learning",
        "excerpt": "Learning something new can be an exciting journey. Join me as I share my recent experiences and discoveries.",
        "content": """
          Learning something new can be an exciting journey, whether it's exploring a new coding language or discovering a new hobby. In this post, I'll share my recent experiences and discoveries, from diving into new technologies to exploring different aspects of life. If you're curious about the joy of learning and exploring, you're in for an exciting read!
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpeg",
        "author": "Prakhar",
        "date": date(2020, 8, 5),
        "title": "Embracing the Beauty of Nature",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Nature is a source of endless wonder and inspiration. The tranquility of the woods, the beauty of the mountains, and the serenity of the lakes all have a unique charm. In this post, I'll share my love for nature and the profound experiences it offers. Join me in embracing the beauty of the natural world and discovering the peace it can bring to our lives.
        """
    }
]



def get_date(post):
    return post["date"]


# Create your views here.


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
