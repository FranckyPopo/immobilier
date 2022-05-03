from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import FormPostAd
from .models import PostAd

class PostAdFormPage(View):
    template_name = "post_ad/post_ad_post.html"
    class_form = FormPostAd
    
    def get(self, request):
        form = self.class_form()
        return render(request, self.template_name, context={"form": form})
    
    def post(self, request):
        data = {
            "city": request.POST.get("city"),
            "house": request.POST.get("house"),
            "title_ad": request.POST.get("title_ad"),
            "description_ad": request.POST.get("description_ad"),
            "user": request.user,
            "price_ad": request.POST.get("price_ad"),
            "user_id_ad": request.user.id,
            "estate_type": request.POST.get("estate_type"),
        }
        print(request.user.id)
        form = self.class_form(data, request.FILES)        
        

        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect("home")
        return render(request, self.template_name, context={"form": form})

class PostAdUpdate(View):
    template_name = "post_ad/post_ad_modified.html"
    class_model = FormPostAd
    
    def get(self, request, number_ad):
        data_post_ad = PostAd.objects.get(id=number_ad)
        form = self.class_model(instance=data_post_ad)
        return render(request, self.template_name, context={"form": form, "number_ad": number_ad})
    
    def post(self, request, number_ad):
        data_post_ad = PostAd.objects.get(id=number_ad)
        form = self.class_model(request.POST, request.FILES, instance=data_post_ad)

        if form.is_valid():
            form.save(commit=False)
            form.uploder = request.user
            form.save()
            return redirect("poster_list") 
        return render(request, self.template_name, context={"form": form})
    


class PostAdDelete(View):
    template_name = "post_ad/post_ad_delete.html"
    class_model = PostAd
    
    def get(self, request, number_ad):
        post_ad = self.class_model.objects.get(id=number_ad)
        return render(request, self.template_name, context={"post_ad": post_ad})
    
    def post(self, request, number_ad):
        post_ad = self.class_model.objects.get(id=number_ad)
        post_ad.delete()
        return redirect("poster_list")


def post_ad_post_list(request):
    post_ad = PostAd.objects.all()
    return render(request, "post_ad/post_ad_poster_list.html", context={"post_ad": post_ad})


def post_ad_post_detailed(request, number_ad):
    post_ad = PostAd.objects.get(id=number_ad)
    return render(request, "post_ad/post_ad_detailed.html", context={"post_ad": post_ad})