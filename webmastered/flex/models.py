from django.db import models
from django.http import HttpResponseRedirect
from django.contrib import messages

from wagtail.admin.panels import StreamFieldPanel, FieldPanel
from wagtail.models import Page

from theme.flex_blocks import flexpage_content_streamfield
from forms.forms import ContactForm

class FlexPage(Page):
    """Model for a flexible page"""
    template = "flex.html"

    content = flexpage_content_streamfield

    content_panels = Page.content_panels + [
        StreamFieldPanel(
            'content',
            heading="Content Section",
            classname="collapsible",
        )
    ]

    class Meta:
        verbose_name = "Flexible Page"
        verbose_name_plural = "Flexible Pages"


class ExternalPage(Page):
    page_description = "Use this page for linking pages from external services within this domain"

    external_page_slug = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="External page slug",
        help_text="Enter the slug of the external page."
    )

    content_panels = Page.content_panels + [
        FieldPanel("external_page_slug"),
    ]

    def serve(self, request, *args, **kwargs):
        external_page_url = '/' + self.external_page_slug
        return HttpResponseRedirect(external_page_url)

    class Meta:
        verbose_name = "External Page"
        verbose_name_plural = "External Pages"


class ExternalWebsite(Page):
    page_description = "Use this page for linking external websites"

    external_page_url = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="External page URL",
        help_text="Enter the URL of the external page."
    )

    content_panels = Page.content_panels + [
        FieldPanel("external_page_url"),
    ]

    def serve(self, request, *args, **kwargs):
        return HttpResponseRedirect(self.external_page_url)

    def get_sitemap_urls(self, request=None):
        return []

    class Meta:
        verbose_name = "External Website"
        verbose_name_plural = "External Websites"


class ContactPage(Page):
    page_description = "This page has an embedded 'contact-us' form"
    max_count = 1
    template = "contact.html"

    content_panels = Page.content_panels

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = ContactForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                form.save()
                form = ContactForm()
                messages.success(request, "Your enquiry form has been submitted successfully, we'll be in touch with "
                                          "you shortly.")
                # redirect to a new URL:
                context['form_submitted'] = True

        # if a GET (or any other method) we'll create a blank form
        else:
            form = ContactForm()
            context['form_submitted'] = False

        context['form'] = form
        return context

    class Meta:
        verbose_name = "Contact Page"
        verbose_name_plural = "Contact Pages"
