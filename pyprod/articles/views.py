from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404

from .models import Subject, Article
from . import forms


class CoreSubjectsView(View):
    template_name = "articles/core_subjects.html"

    def get(self, request, *args, **kwargs):
        subjects = Subject.objects.filter(parent__isnull=True)
        return render(request, self.template_name, {"subjects": subjects})


class SubjectView(View):
    template_name = "articles/subject.html"

    def get(self, request, slug, *args, **kwargs):
        subject = get_object_or_404(Subject, slug=slug)
        child_subjects = Subject.objects.filter(parent=subject)
        articles = Article.objects.filter(subject=subject)
        context = {
            "subject": subject,
            "child_subjects": child_subjects,
            "articles": articles
        }
        return render(request, self.template_name, context)


class ArticleView(View):
    template_name = "articles/articles/detail.html"

    def get(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        return render(request, self.template_name, {"article": article})


class CreateArticleView(View):
    template_name = "articles/articles/create.html"

    def get(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        return render(request, self.template_name, {"article": article})


class EditArticleView(View):
    template_name = "articles/articles/edit.html"

    def get(self, request, slug, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)
        form = forms.ArticleForm(instance=article)
        print(form)
        context = {"article": article, "form": form}
        return render(request, self.template_name, context)
