from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . models import Post, Question, Answer
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request, 'review/test.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'review/test.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Answer

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Answer
    fields=['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Answer
    fields=['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Answer
    success_url = '/'
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'review/about.html', {'title': 'about'})



def question(request,pk,qslug):
    context = {
        'question': Question.objects.get(qid=pk,slug=qslug)
    }
    return render(request, 'review/question.html', context)

class QuestionListView(ListView):
    model = Question
    template_name = 'review/question.html'
    context_object_name = 'question'
    ordering = ['-date_posted']


def answer(request,pk):
    context = {
        'answer': Answer.objects.all()
    }
    return render(request, 'review/answer.html', context)

class AnswerListView(ListView):
    model = Answer
    template_name = 'review/answer.html'
    context_object_name = 'answer'
    ordering = ['-date_posted']