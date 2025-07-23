from django.urls import path
from .views import keyword_match_view, chat_history_view

urlpatterns = [
    path('kmp/', keyword_match_view, name='kmp_test'),
    path('chat-history/', chat_history_view),
    path('chat-history/', chat_history_view, name='chat_history'),
]
