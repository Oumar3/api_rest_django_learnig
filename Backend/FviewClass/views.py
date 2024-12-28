from django.shortcuts import render
from django.views import View
from .models import Article
from .forms import ArticleForm
# Create your views here.

class ArticleViews(View):
    template_name = 'article/index.html'
    form_class = ArticleForm
    initial = {"title":"test","content":"test","img":"test","author":"test","date":"2022-01-01"}
    def get(self,request,*args,**kwargs):
        form = self.form_class(initial=self.initial)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return render(request,self.template_name,{'form':self.form_class})
            
        return render(request,self.template_name,{'form':form})
    
    def put(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return render(request,self.template_name,{'form':self.form_class})
            
        return render(request,self.template_name,{'form':form})
    
   
    

