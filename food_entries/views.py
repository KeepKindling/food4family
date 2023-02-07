from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Entry

from django.shortcuts import redirect

def homepage(request):
    response = redirect('accounts/signup')
    return response

class EntryList(generic.ListView):
    model = Entry
    queryset = Entry.objects.filter(status=1).order_by('-created_on')
    template_name = 'base.html'


# This class is to display the details of a recipe
# that has been clicked on by a user.

# class EntryDetail(View):
#     def get(self, request, *args, **kwargs):
#         queryset = Entry.objects.filter(status=1)
#         entry = get_object_or_404(queryset, slug=slug)

#         return render(
#             request,
#             "recipe_details.html",
#             {
#                 "title": title,
#                 "author": author,
#                 "created_on": created_on,
#                 "updated_on": updated_on,
#                 "description": description,
#             }
#         )
