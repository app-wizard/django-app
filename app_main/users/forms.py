from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


from users.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")

    # username = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "autofocus": True,
    #             "class": "form-control",
    #             "placeholder": "Username",
    #         }
    #     )
    # )
    # password = forms.CharField(
    #     label=("Password"),
    #     strip=False,
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "autocomplete": "current-password",
    #             "class": "form-control",
    #             "placeholder": "Password",
    #         }
    #     ),
    # )

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )
