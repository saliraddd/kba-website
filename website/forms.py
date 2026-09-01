from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage

        fields = [
            "name",
            "company",
            "phone",
            "email",
            "subject",
            "message",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "نام و نام خانوادگی"}
            ),

            "company": forms.TextInput(
                attrs={"placeholder": "نام شرکت"}
            ),

            "phone": forms.TextInput(
                attrs={"placeholder": "شماره تماس"}
            ),

            "email": forms.EmailInput(
                attrs={"placeholder": "ایمیل"}
            ),

            "subject": forms.TextInput(
                attrs={"placeholder": "موضوع درخواست"}
            ),

            "message": forms.Textarea(
                attrs={
                    "placeholder": "توضیحات پروژه یا درخواست شما",
                    "rows": 6,
                }
            ),
        }