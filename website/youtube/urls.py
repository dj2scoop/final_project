from django.conf.urls import patterns, url, include
from django.views.generic import ListView

from youtube.models import Search
from youtube.forms import SearchForm
from youtube.views import SearchView

from youtube.models import Results
from youtube.forms import ResultsForm
from youtube.views import ResultsView

from youtube.forms import VideoForm
from youtube.views import VideoView

from youtube.models import CredentialsModel

from registration.views import register

urlpatterns = patterns('',
    # List view for all searches:
    url(r'^history/$',
        ListView.as_view(
            queryset=Search.objects.all(),
            context_object_name="searches",
            template_name="youtube/history_list.html"
        ),
        name="history_list"),
    url(r'^$',
        SearchView.as_view(
            model=Search,
            form_class=SearchForm,
            template_name="youtube/search_form.html",
            success_url="/results",
        ),
        name="search"),
    url(r'^results/$',
        ResultsView.as_view(
            model=Results,
            form_class=ResultsForm,
            template_name="youtube/result_list.html",
            success_url="/video",
        ),
        name="result_list"),
    url(r'^success/$',
        SearchView.as_view(
            model=Search,
            form_class=SearchForm,
            template_name="registration/registration_complete.html",
        ),
        name="register_success"),
    url(r'^video/$',
        VideoView.as_view(
            model=Results,
            form_class=VideoForm,
            template_name="youtube/video_player.html",
        ),
        name="video_play"),
)
