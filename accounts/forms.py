from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

    class Meta:
        fields = ('username','email','password1','password2')
        model  = get_user_model()

    """
    the def init give label to fields that i choose from contib.auth
    """

    def __init__ (self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].lable  = 'Display Name'
        self.fields['email'].lable     = 'Email Address'
        self.fields['password1'].lable = 'Enter Password'
        self.fields['password2'].lable = 'Confirm Password'
