from django.shortcuts import render
from django.views.generic import DetailView
from .models import Category

class CategoryView(DetailView):
    model = Category