
# Create your own urls inside your app because maybe we can have different apps inside the same django projects

from django.urls import path
from . import views 


app_name = "myapp"

urlpatterns = [
    path('', views.index, name = "index"),
    # ex: /myapp/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /myapp/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /myapp/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]









7y