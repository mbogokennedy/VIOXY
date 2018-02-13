from django.shortcuts import render

# Create your views here.
# class IndexView(generic.ListView):
#     template_name = 'mine/index.html'
#     context_object_name = 'latest_question_list'

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by('-pub_date')[:5]
def index(request):
    context = {}
    template='index.html'
    return render(request,template,context)
def about(request):
    context = {}
    template='profiles/about.html'
    return render(request,template,context)

