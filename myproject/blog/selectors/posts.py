from django.db.models import QuerySet

from myproject.blog.models import Post

def get_posts() -> QuerySet[Post]:
    return Post.objects.all()