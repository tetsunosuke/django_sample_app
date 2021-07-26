from django.urls import path

from . import views

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('add/<int:question_id>/<int:x>', views.add, name='add'),
    path('buy/<int:question_id>/<int:x>', views.buy, name='buy'),
]
