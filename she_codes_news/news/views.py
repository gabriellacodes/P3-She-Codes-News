from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm

# good shit https://ccbv.co.uk

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    # these guys are methods
    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # pulls the first 4 stories to show up the top, - being to sort in descending order
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        # displays all news stories below
        context['all_stories'] = NewsStory.objects.order_by('-pub_date')
        return context    

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'