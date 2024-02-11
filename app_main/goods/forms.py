from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["body"].label = ""  # Измените метку поля 'body'
        self.fields["body"].widget.attrs.update(
            {
                "class": "form-control",
                "rows": "5",
                "placeholder": "Enter your comment here...",
            }
        )
