from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from django.utils.translation import get_language,activate,gettext_lazy
from django.utils.translation import get_language_from_request

# Create your views here.

def translate(language,string):
    cur_language = get_language()

    print(">>>translate",cur_language)
    try:
        activate(language)
        text = _(string)
        cur_language = get_language()
        print(">>>translate",cur_language)
        print(">>>>text",language,text,string)
    except Exception as e:
        print(">>>eeee",e)
    finally:
        activate(cur_language)
        print(">>>>testing\n\n\n",text,string)

    return text

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        # language = kwargs.get('lang','en')
        language = get_language_from_request(self.request)

        print(">>>language",language)
        
        context['page'] = translate(language=language,string="Hello, I am jay from india")
        return context

def about(request, count):
    page = gettext_lazy('Hello, I am jay from india')
    return HttpResponse(page)