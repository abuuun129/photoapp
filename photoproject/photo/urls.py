from django.urls import path
from . import views

#URLパターンを玉引きできるように名前を付ける
app_name = 'photo'

#URLパターンを登録する変数
urlpatterns = [
    #photoアプリへのアクセスはviewsモジュールのindexViewを実行
    path('', views.IndexView.as_view(), name = 'index'),

]
