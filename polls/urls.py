from django.urls import path

from . import views

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('update/<int:question_id>', views.update, name='update'),
    path('update_lock/<int:question_id>', views.update_lock, name='update_lock'),
]
