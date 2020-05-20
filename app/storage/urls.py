from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('teams/', views.TeamListView.as_view(), name='teams'),
    path('team/<int:pk>', views.TeamDetailView.as_view(), name='team-detail'),
    path('mysecrets/', views.SecretsByUserListView.as_view(), name='my-secrets'),
    path('mysecret/<uuid:pk>', views.SecretDetailView.as_view(), name='my-secret-detail'),
    path(r'mygroups/', views.TeamsByUserListView.as_view(), name='my-groups'),
]
