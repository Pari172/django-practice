from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string    # this work is already done by render
month_and_chanllenge = {
    'january':'january challenge is here',
    'february':'february challenge is here',
    'march':'march challenge is here',
    'april':'april challenge is here',
    'may':'may challenge is here',
    'june':'june challenge is here',
    'july':'july challenge is here',
    'august':'august challenge is here',
    'september':'september challenge is here',
    'october':'october challenge is here',
    'november':'november challenge is here',
    'december': None,
}
# Create your views here.
def index(request):
    # return HttpResponse("You are inside year_challenge app")
    months = list(month_and_chanllenge.keys())
    list_items=""
    # for month in months:
    #     capitolized_month = month.capitalize()
    #     month_path = reverse("monthly-challenge",args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitolized_month}</a></li>"
    # res_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(res_data)
    return render(request,'year_challenge/index.html',{
        "months": months
    })

def monthly_challenge(request,month):
    try:
        challenge_text = month_and_chanllenge[month]
        months = list(month_and_chanllenge.keys())
        return render(request,'year_challenge/challenge.html',{
            "text":challenge_text,
            "month":month,
            "month_number":months.index(month)
        })
    except Exception:
        return HttpResponse("Invalid month by string!")

    
def monthly_challenge_by_number(request,month):
    try:
        months = list(month_and_chanllenge.keys())
        # return HttpResponse(month_and_chanllenge[months[month-1]])
        return HttpResponseRedirect(
            reverse('year_challenge:monthly_challenge',args=[months[month-1]])
        )
    except Exception:
        return HttpResponse("Invalid month by int!")