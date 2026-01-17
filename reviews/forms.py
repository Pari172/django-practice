from django import forms
from .models import Review

# when we want to create form without model
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(
#         label='Your Name',
#         max_length=10,
#         error_messages={
#             'required': 'Your name must not be empty',
#             'max_length': 'Please enter a shorter name!'
#         }
#     )

#     review_text = forms.CharField(
#         label="Your Feedback",
#         widget=forms.Textarea,  
#         max_length=200,       
#     )

#     rating = forms.IntegerField(
#         label = 'Rating',
#         min_value = 1,
#         max_value = 5,
#     )


# when we want to create form from existing model
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = ['user_name', ''] When we can add individually 
        fields = '__all__' # when we want to include all fields of model
        # exclude = ['rating'] when we want to not include perticuler fields

        # When we want to add lables because if we dont add our own labels we will get lables same as field name
        labels = {
            'user_name' : 'Your Name',
            'review_text' : 'Tour Feedback',
            'rating' : 'Please provide rating'
        }

        # when we want to show error massages according to our need
        error_messages =  {
            "user_name" : {
                "required" : "Your name must not be empty!",
                "max_length" : "Please enter a shorter name"
            }
        }           