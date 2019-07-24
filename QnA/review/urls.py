from django.urls import path
from . import views
from . views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    QuestionListView,
    AnswerListView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/<slug:qslug>', QuestionListView.as_view(), name='question-home'),
    path('post/<int:pk>/question/', AnswerListView.as_view(), name='answer-home'),
    path('post/<int:pk>/question/answer/', PostDetailView.as_view(), name='answer-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='answer-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='answer-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about')
]