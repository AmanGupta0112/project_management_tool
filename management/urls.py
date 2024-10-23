from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from . import views

urlpatterns = [
    # User Endpoints
    path("users/", views.user_list, name="user-list"),
    path("users/<int:pk>/", views.user_detail, name="user-detail"),
    # Project Endpoints
    path("projects/", views.project_list, name="project-list"),
    path("projects/<int:pk>/", views.project_detail, name="project-detail"),
    # Task Endpoints
    path("projects/<int:project_id>/tasks/", views.task_list, name="task-list"),
    path("tasks/<int:pk>/", views.task_detail, name="task-detail"),
    # Comment Endpoints
    path("tasks/<int:task_id>/comments/", views.comment_list, name="comment-list"),
    path("comments/<int:pk>/", views.comment_detail, name="comment-detail"),
    # JWT Endpoints
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
