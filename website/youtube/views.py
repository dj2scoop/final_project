from django.views.generic import CreateView

from youtube.forms import SearchForm
from youtube.models import Search

# Create your views here.

class SearchView(CreateView):
    """View for searching YouTube"""

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.searcher = self.request.user
        self.object.save()
        return super(SearchView, self).form_valid(form)


class ResultsView(CreateView):
    """View for viewing YouTube results"""
    pass


class VideoView(CreateView):
    """View for viewing YouTube videos"""
    pass
