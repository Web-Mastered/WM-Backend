from theme.home_blocks import homepage_content_blocks
from wagtail.blocks import StructBlock, RichTextBlock, DecimalBlock, ListBlock, ChoiceBlock, CharBlock, PageChooserBlock
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock


class Pricing(StructBlock):
    """Pricing block"""

    class PricingTable(StructBlock):
        class PricingTier(StructBlock):
            class TierFeatures(StructBlock):
                feature_text = RichTextBlock(
                    blank=True,
                    null=True,
                    features=[
                        'emphasis',
                        'italic',
                        'link',
                        'document-link',
                        'code',
                        'superscript',
                        'subscript',
                        'strikethrough',
                    ],
                    verbose_name="Feature text",
                    help_text="Give a description of this feature, this will be displayed on the pricing table.",
                )

                feature_type = ChoiceBlock(
                    choices=[
                        ('inc', 'Included'),
                        ('add', 'Addition'),
                    ],
                    help_text="An icon will be added beside the feature description, when 'Included' is selected, "
                              "a tick icon appears, when 'Addition' is selected, a plus icon appears. "
                )

                class Meta:
                    icon = "pick"
                    label = "Feature"

            name = RichTextBlock(
                blank=True,
                null=True,
                features=[
                    'superscript',
                    'subscript',
                    'strikethrough',
                ],
                verbose_name="Tier name",
                help_text="Enter the name of this tier.",
            )

            price = DecimalBlock(
                required=True,
                min_value=0,
                max_digits=6,
                decimal_places=2,
                help_text="Enter the price p/m of this tier."
            )

            description = RichTextBlock(
                blank=True,
                null=True,
                features=[
                    'emphasis',
                    'italic',
                    'link',
                    'document-link',
                    'code',
                    'superscript',
                    'subscript',
                    'strikethrough',
                ],
                verbose_name="Tier description",
                help_text="Give a description for this pricing tier",
            )

            highlight_tier_text = CharBlock(
                max_length=50,
                null=True,
                blank=True,
                required=False,
                verbose_name="Highlight text",
                help_text="If you'd like to add a highlight to this tier, enter the highlight text here.",
            )

            features = ListBlock(
                TierFeatures()
            )

            class Meta:
                icon = "tag"
                label = "Tier"

        name = CharBlock(
            max_length=50,
            null=True,
            blank=True,
            verbose_name="Table name",
            help_text="Give a name for this pricing table.",
        )

        heading = RichTextBlock(
            blank=True,
            null=True,
            features=[
                'emphasis',
                'italic',
                'link',
                'document-link',
                'code',
                'superscript',
                'subscript',
                'strikethrough',
            ],
            verbose_name="Table heading",
            help_text="Give a heading for this pricing table",
        )

        description = RichTextBlock(
            blank=True,
            null=True,
            features=[
                'emphasis',
                'italic',
                'link',
                'document-link',
                'code',
                'superscript',
                'subscript',
                'strikethrough',
            ],
            verbose_name="Table description",
            help_text="Give a description for this pricing table",
        )

        tiers = ListBlock(
            PricingTier()
        )

        class Meta:
            icon = "table"
            label = "Pricing Table"

    heading = RichTextBlock(
        blank=True,
        null=True,
        features=[
            'emphasis',
            'italic',
            'link',
            'document-link',
            'code',
            'superscript',
            'subscript',
            'strikethrough',
        ],
        verbose_name="Table heading",
        help_text="Give a heading for this pricing block",
    )

    pricing_tables = ListBlock(
        PricingTable()
    )

    class Meta:
        template = "blocks/flex/pricing.html"
        icon = "sterling-sign"
        label = "Pricing"


class FrequentlyAskedQuestions(StructBlock):
    """An FAQ block"""

    class QuestionAndAnswer(StructBlock):
        """A question and an answer"""
        question = RichTextBlock(
            blank=True,
            null=True,
            features=[
                'emphasis',
                'bold',
                'italic',
                'link',
                'document-link',
                'code',
                'superscript',
                'subscript',
                'strikethrough',
            ],
            verbose_name="Question",
            help_text="Enter a question.",
        )

        answer = RichTextBlock(
            blank=True,
            null=True,
            features=[
                'emphasis',
                'bold',
                'italic',
                'link',
                'document-link',
                'code',
                'superscript',
                'subscript',
                'strikethrough',
            ],
            verbose_name="Answer",
            help_text="Enter an answer to the question.",
        )

    heading = RichTextBlock(
        blank=True,
        null=True,
        features=[
            'emphasis',
            'bold',
            'italic',
            'link',
            'document-link',
            'code',
            'superscript',
            'subscript',
            'strikethrough',
        ],
        verbose_name="Heading",
        help_text="Enter a heading for this FAQ block.",
    )

    question_and_answer = ListBlock(
        QuestionAndAnswer()
    )

    class Meta:
        template = "blocks/flex/frequently_asked_questions.html"
        icon = "help"
        label = "FAQs"


class Timeline(StructBlock):
    """Block to display a timeline of events"""

    class Event(StructBlock):
        """En event"""
        name = CharBlock(
            max_length=50,
            required=False,
            verbose_name="Name",
            help_text="Give a name for this event.",
        )

        image = ImageChooserBlock(
            required=True,
            verbose_name="Image",
            help_text="This image will be displayed beside the event name, heading and content.",
        )

        heading = RichTextBlock(
            required=True,
            features=[
                'emphasis',
                'bold',
                'italic',
                'link',
                'document-link',
                'code',
                'superscript',
                'subscript',
                'strikethrough',
            ],
            verbose_name="Heading",
            help_text="Enter a heading for this event.",
        )

        content = RichTextBlock(
            blank=True,
            null=True,
            features=[
                'emphasis',
                'bold',
                'italic',
                'link',
                'document-link',
                'code',
                'superscript',
                'subscript',
                'strikethrough',
            ],
            verbose_name="Content",
            help_text="Enter content for this event.",
        )

        button_content = RichTextBlock(
            required=False,
            features=[
                'emphasis',
                'italic',
                'link',
                'document-link',
                'code',
                'superscript',
                'subscript',
                'strikethrough',
            ],
            verbose_name="Button text",
            help_text="Optional: You can add a button to display below the content. Enter the text to go inside the button",
        )

        button_link = PageChooserBlock(
            required=False,
            verbose_name="Button link",
            help_text="Optional: You can link a page to this button."
        )

        class Meta:
            icon = "date"
            label = "Event"

    heading = RichTextBlock(
        blank=True,
        null=True,
        features=[
            'emphasis',
            'bold',
            'italic',
            'link',
            'document-link',
            'code',
            'superscript',
            'subscript',
            'strikethrough',
        ],
        verbose_name="Heading",
        help_text="Enter a heading for this timeline block.",
    )

    events = ListBlock(
        Event()
    )

    class Meta:
        template = "blocks/flex/timeline.html"
        icon = "timeline"
        label = "Timeline"


class StaffListing(StructBlock):
    """Block that lists all the staff"""
    heading = RichTextBlock(
        required=True,
        features=[
            'emphasis',
            'bold',
            'italic',
            'link',
            'document-link',
            'code',
            'superscript',
            'subscript',
            'strikethrough',
        ],
        verbose_name="Heading",
        help_text="Enter a heading for this block.",
    )

    class Meta:
        template = "blocks/flex/staff_listing.html"
        icon = "group"
        label = "Staff Listing"


flexpage_content_blocks = homepage_content_blocks + [
    ("flexpage_pricing", Pricing()),
    ("flexpage_frequentlyaskedquestions", FrequentlyAskedQuestions()),
    ("flexpage_timeline", Timeline()),
    ("flexpage_stafflisting", StaffListing()),
]

flexpage_content_streamfield = StreamField(
    flexpage_content_blocks,
    null=True,
    blank=True,
    help_text="Choose blocks to be shown in the body."
)
