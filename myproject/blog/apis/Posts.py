from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from drf_spectacular.utils import extend_schema

from myproject.api.pagination import LimitOffsetPagination
from myproject.blog.models import Post
from myproject.blog.services.posts import create_post
from myproject.blog.selectors.posts import get_posts

class PostApi(APIView):
    
    class Pagination(LimitOffsetPagination):
        default_limit = 5

    
    class InputSerializers(serializers.Serializer):
        title = serializers.CharField(max_length=255)

    class OutPutserilizers(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ('title', "created_at", "updated_at")

    @extend_schema(request=InputSerializers, responses=OutPutserilizers)
    def post(self, request):
        serializer = self.InputSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            query = create_post(title=serializer.validated_data.get("title"))
        except Exception as ex:
            return Response(f"database error {ex}",
                status=status.HTTP_400_BAD_REQUEST)
        
        return Response(self.OutPutserilizers(query, context={'request': request}).data)
    
    @extend_schema(request=InputSerializers, responses=OutPutserilizers)
    def get(self, request):
        query = get_posts()
        return Response(self.OutPutserilizers(query, context={'request': request}, many=True).data)