from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PageChooserPanel, StreamFieldPanel

from theme.home_blocks import homepage_content_streamfield


class HomePage(Page):
    """Home page class"""

    template = "home.html"
    max_count = 1

    hero_title = RichTextField(
        blank=True,
        null=True,
        features=[
            'emphasis',
        ],
        verbose_name="Title",
        help_text="This text will be displayed in the 'title' section of the hero.",
    )
    hero_subtitle = RichTextField(
        blank=True,
        null=True,
        verbose_name="Subtitle",
        help_text="This text will be displayed below the title in the 'subtitle' section of the hero.",
    )
    hero_button_text = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Button text",
        help_text="This text will be displayed inside the button in the hero section.",
    )
    hero_button_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Button link",
        help_text="Choose a page to be opened when the user clicks the button in the hero.",
    )

    content = homepage_content_streamfield

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel(
                  'hero_title'
                ),
                FieldPanel(
                    'hero_subtitle'
                ),
                FieldPanel(
                    'hero_button_text'
                ),
                PageChooserPanel(
                    'hero_button_page'
                )
            ],
            heading="Hero Section",
            classname="collapsible"
        ),
        StreamFieldPanel(
            'content',
            heading="Content Section",
            classname="collapsible",
        )
    ]