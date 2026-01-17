from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
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
class ReviewView(View):
    def get(self,request):
        form = ReviewForm()
        return render(request, "reviews/index.html", {
            "form" : form
        })

    def post(self,request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/reviews/thank-you')

def thank_you(request):
    # entered_username = request.POST['username'] this line will cause error because after doing redirect its a GET req not POST req
    return render(request, "reviews/thank_you.html",{
        # 'username': entered_username
    })