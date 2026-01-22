from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
# Create your views here.

# This I created before learning about ModelForm
def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        # entered_username = request.POST['username']
        # if entered_username=="":
        #     return render(request,'reviews/index.html',{
        #         'has_error': True
        #     })
        if form.is_valid():
            print(form.cleaned_data)
            # return render(request, "reviews/thank_you.html",{
            #     'username':form.cleaned_data
            # })
            review = Review(
                user_name=form.cleaned_data['user_name'],
                review_text=form.cleaned_data['review_text'],
                rating=form.cleaned_data['rating']
            )
            review.save()
            return HttpResponseRedirect("/reviews/thank-you")
    else:
        form = ReviewForm()
    return render(request,'reviews/index.html',{
        'form': form
    })


#This I created after learning model form
def review1(request):
    if request.method == "POST":
        # when we want to update exisiting data
        # exisiting_model = Review.objects.get(pk=1)
        # form = ReviewForm(request.POST, instance=exisiting_model)
        form = ReviewForm(request.POST)
        if form.is_valid():
            #print(form) # this statement will print complete form with filled data
            form.save()
            return HttpResponseRedirect("/reviews/thank-you")
    else:
        form = ReviewForm()
    return render(request,'reviews/index.html',{
        'form': form
    })
    
 
# This is a class based view, it automatically handle get and post methods, we just need to create get and post funtions and django do it all
# class ReviewView(View):
#     def get(self,request):
#         form = ReviewForm()
#         return render(request, "reviews/index.html", {
#             "form" : form
#         })

#     def post(self,request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/reviews/thank-you')

# above ReviewView can be rplaced with bellow class view using FormView
class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/index.html"
    success_url = "thank-you"
    
    def form_invalid(self, form):
        form.save()
        return super().form_invalid(form)
    
    

# def thank_you(request):
#     # entered_username = request.POST['username'] this line will cause error because after doing redirect its a GET req not POST req
#     return render(request, "reviews/thank_you.html",{
#         # 'username': entered_username
#     })


# commenting this out because bellow is TemplateView which is used to directly rendering the templates
# class ThankYou(View):
#     def get(self, request):
#         return render(request,'reviews/thank_you.html')


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works!"
        return context

# commenting this out after knowing about ListView  
# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context

class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews" # by defualt it is 'object_list'
    def get_ordering(self):
        return ['id']

class SingleReviewView(TemplateView):
    template_name = "reviews/single_review.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        review = Review.objects.get(pk=review_id)
        context["review"] = review
        favorite_id = self.request.session.get("favorite_review")
        context["is_favorite"] = favorite_id==str(review_id)
        return context
    
class AddFevoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        fev_review = Review.objects.get(pk=review_id)
        request.session["favorite_review"]=review_id
        return HttpResponseRedirect("/reviews/"+review_id)