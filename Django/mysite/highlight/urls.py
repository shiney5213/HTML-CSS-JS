from django.urls import path
from . import views



urlpatterns = [
    path('', views.highlightView.as_view(), name = 'highlight'),
    path('subtitle', views.subtitleView.as_view(), name = 'subtitle'),
    # path('output', views.output),



]