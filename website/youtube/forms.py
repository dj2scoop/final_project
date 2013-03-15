from django import forms

from youtube.models import Search
from youtube.models import Results
from youtube.models import Video
import search

class SearchForm(forms.ModelForm):
    """allow search entries to be catalogued so that they can re-used in the history view"""

    class Meta:
        model = Search
        fields = ('search', )


class ResultsForm(forms.ModelForm):
    """show results from the YouTube search"""
    result = search.youtube_search('Tool', 10)



class VideoForm(forms.ModelForm):
    """show video player"""
    pass
