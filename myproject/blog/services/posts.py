from django.db.models import QuerySet

from myproject.blog.models import Post

def create_post(title: str) -> QuerySet[Post]:
    return Post.objects.create(title=title)