from django import forms
from django.conf import settings

from forms.models import Contact

from sendgrid import SendGridAPIClient



class ContactForm(forms.ModelForm):

    protect = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': "wm-contact-protect form-checkbox hidden",
                'style': "autocomplete=\"off\" tabindex=\"-1\"",
                'value': 1,
            },
        )
    )

    gdpr_consent = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(
            attrs={
                'class': "wm-contact-gdpr-consent form-checkbox focus:ring-0",
            },
        ),
        label="To respond, we need to store this submission. Is that ok?",
    )

    marketing_consent = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': "wm-contact-marketing-consent form-checkbox focus:ring-0",
            },
        ),
        label="Would you like to join our mailing list?",
    )

    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'message',
            'gdpr_consent',
            'marketing_consent',
            'protect'
        ]
        labels = {
            'name': 'How shall we address you?',
            'email': 'How shall we contact you?',
            'message': 'How can we help you with your project?',
        }
        textClassnames = "w-full font-paragraph border-0 border-b-2 focus:ring-0 placeholder:text-gray-400 " \
                     "border-gray-300 focus:border-wm-blue text-2xl"
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': "wm-contact-name form-input" + " " + textClassnames,
                    'placeholder': "Your name",
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': "wm-contact-email form-input" + " " + textClassnames,
                    'placeholder': "Your email address",
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': "wm-contact-message form-textarea resize-none" + " " + textClassnames,
                    'placeholder': "Tell us about your project",
                    'rows': 1,
                }
            ),
        }

    def clean_gdpr_consent(self):
        consented = self.cleaned_data.get('gdpr_consent')
        if not consented:
            raise forms.ValidationError('To send this form, you must tick this box.')
        return consented

    def save(self, commit=True):
        if not self.cleaned_data.get('protect'):
            save_status = super().save(commit)
            if self.cleaned_data.get('marketing_consent'):
                if " " in self.instance.name:
                    first_name, last_name = self.instance.name.split(" ", maxsplit=1)
                else:
                    first_name = self.instance.name
                    last_name = None
                email = self.instance.email

                sg = SendGridAPIClient(settings.SENDGRID_API_KEY)

                data = {
                    "list_ids": [
                        settings.SENDGRID_MARKETING_LIST_ID,
                    ],
                    "contacts": [
                        {
                            "email": email,
                            "first_name": first_name,
                        }
                    ]
                }
                if last_name:
                    data["contacts"][0]["last_name"] = last_name

                sg.client.marketing.contacts.put(
                    request_body=data
                )

            return save_status


