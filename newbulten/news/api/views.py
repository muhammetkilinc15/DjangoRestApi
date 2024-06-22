from rest_framework import status
from rest_framework.response import Response # redirect gibi
from rest_framework.decorators import api_view
from news.models import Article
from news.api.serializers import ArticleSerializer


@api_view(['GET','POST'])
def Article_list_create_api_view(request):
    
    if request.method == 'GET':
        articles = Article.objects.filter(isActive=True) # burada nesnelerden olusan query set donecek
        serializer = ArticleSerializer(articles,many=True) # query set ? 
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=None,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def GetArticle(request,articleid):
    article = Article.objects.filter(pk=articleid)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
            
