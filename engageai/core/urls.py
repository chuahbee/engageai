from django.urls import path
from .views import keyword_match_view

urlpatterns = [
    path('kmp/', keyword_match_view, name='kmp_test'),
]
