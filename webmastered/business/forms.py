from django import forms

from .models import ServerUpgrade


class ServerUpgradeForm(forms.ModelForm):
    readOnlyMode = True
    class Meta:
        model = ServerUpgrade
        fields = "__all__"
        widgets = {
            'user': forms.HiddenInput(),
            'comments': forms.Textarea(),
            'request_datetime': forms.HiddenInput(),
            'report_submitted': forms.HiddenInput(),
            'scheduled_datetime': forms.HiddenInput(),
            'is_finished': forms.HiddenInput(),
        }

    def __init__(self, *args, **kws):
        self.user = kws.pop('user')
        self.readOnlyMode = kws.pop('readOnlyMode')
        super().__init__(*args, **kws)
        self.fields['user'].initial = self.user
        self.fields['is_finished'].initial = False
        self.fields['comments'].label = "Comments"
        self.fields['comments'].widget.attrs['class'] = 'form-textarea w-full'
        if self.readOnlyMode:
            self.fields['comments'].widget.attrs['readonly'] = 'true'
            self.fields['comments'].widget.attrs['class'] = 'bg-gray-100 border-0'

