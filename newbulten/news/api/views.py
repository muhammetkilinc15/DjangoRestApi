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
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def article_detail_api_view(request,pk):
    try:
        article_instace = Article.objects.get(pk=pk)       
    except:
        return Response(
            {'errors':{
                "code":404,
                "message":f"Can not found this article with pk= {pk}"
                }
            
            },
            status= status.HTTP_404_NOT_FOUND
            )        
    if request.method == 'GET':
        serializer = ArticleSerializer(article_instace)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer = ArticleSerializer(article_instace,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        article_instace.delete()
        return Response(
             { 'errors':{
                "code":204,
                "message":f"Deleted this article with pk= {pk}"
                }
            
            },
            status= status.HTTP_204_NO_CONTENT
        )