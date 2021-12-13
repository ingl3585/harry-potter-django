from django.urls import path
from .views import schools
from .views import houses
from .views import students

urlpatterns = [
    # path('', views.index, name='index'),
    path('schools/', schools.SchoolsView.as_view(), name='index'),
    # path('<int:pk>/', views.show, name='Book-detail'),
    path('schools/<int:pk>/', schools.SchoolView.as_view(), name='School-detail'),
    # path('', views.index, name='index'),
    path('houses/', houses.HousesView.as_view(), name='index'),
    # path('<int:pk>/', views.show, name='Book-detail'),
    path('houses/<int:pk>/', houses.HouseView.as_view(), name='House-detail'),
    # path('', views.index, name='index'),
    path('students/', students.StudentsView.as_view(), name='index'),
    # path('<int:pk>/', views.show, name='Book-detail'),
    path('students/<int:pk>/', students.StudentView.as_view(), name='Student-detail'),
]
