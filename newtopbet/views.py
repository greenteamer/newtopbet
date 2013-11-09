from pages.models import Page
from django.views.generic import ListView

class HomeListView(ListView):
    context_object_name = 'last_pages'
    queryset = Page.objects.all()
    template_name = 'Pages/home.html'

    # def get_context_data(self, **kwargs):
    #     context = super(HomeListView, self).get_context_data(**kwargs)
    #     context['photo_context'] = Photo.objects.all()
    #     context['page_context'] = Page.objects.all()
    #     And so on for more models
    #     return context
