from django.urls import path
from news.api import views
urlpatterns = [
    path('articles/',views.Article_list_create_api_view,name="ListArticles"),
    path('articles/<int>:articleid',views.GetArticle,name="GetArticle")
]
