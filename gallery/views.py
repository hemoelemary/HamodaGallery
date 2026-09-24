from django.views.generic import TemplateView,DetailView,FormView
from .models import Post
from .forms import PostForm
from django.contrib import messages

class Home(TemplateView):
    template_name='index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects']= Post.objects.all().order_by('-id')
        #{{objects}}
        return context


class Details(DetailView):
    model=Post
    template_name='details.html'

class PostView(FormView):
    template_name='post.html'
    form_class=PostForm
    success_url='/'
    def dispatch(self, request, *args, **kwargs):
        self.request=request
        return super().dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        uploadername = form.cleaned_data['uploadername']
        image = form.cleaned_data['image']
        desc =form.cleaned_data['details']
        picname = form.cleaned_data['picname']
        Post.objects.create(uploadername=uploadername,image=image,details=desc,picname=picname)
        messages.add_message(self.request,messages.SUCCESS,'تمت اضافة صورتك بنجاح يا صديقي')
        return super().form_valid(form)