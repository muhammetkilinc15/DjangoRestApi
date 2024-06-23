from django.urls import path
from news.api import views
urlpatterns = [
    path('articles/',views.Article_list_create_api_view,name="ListArticles"),
    path('articles/<int:pk>',views.article_detail_api_view,name="Article-detail")
]
