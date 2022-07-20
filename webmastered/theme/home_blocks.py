from wagtail.blocks import StructBlock, RichTextBlock, ListBlock, CharBlock, PageChooserBlock, StreamBlock
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock

class HeaderAndParagraph(StructBlock):
    """Header and paragraph block"""
    class Paragraph(StructBlock):
        """Paragraph of the block"""
        content = RichTextBlock(
            required=False,
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
            help_text="Enter some content.",
        )

        class Meta:
            icon = "pilcrow"
            label = "Paragraph"

    heading = RichTextBlock(
        required=False,
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
        help_text="Enter a heading for the content.",
    )

    paragraphs = ListBlock(
        Paragraph()
    )

    class Meta:
        template = "blocks/flex/header_and_paragraph.html"
        icon = "pilcrow"
        label = "Heading & Paragraph"

class MultiLevelContent(StructBlock):
    class Heading1(StructBlock):
        heading = RichTextBlock(
            required=False,
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
            verbose_name="Heading 1",
            help_text="Enter a heading for the content.",
        )
        class Meta:
            icon = "pilcrow"
            label = "Heading 1"

    class Heading2(StructBlock):
        heading = RichTextBlock(
            required=False,
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
            verbose_name="Heading 2",
            help_text="Enter a heading for the content.",
        )
        class Meta:
            icon = "pilcrow"
            label = "Heading 2"

    class Heading3(StructBlock):
        heading = RichTextBlock(
            required=False,
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
            verbose_name="Heading 3",
            help_text="Enter a heading for the content.",
        )
        class Meta:
            icon = "pilcrow"
            label = "Heading 3"

    class Heading3(StructBlock):
        heading = RichTextBlock(
            required=False,
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
            verbose_name="Heading 3",
            help_text="Enter a heading for the content.",
        )
        class Meta:
            icon = "pilcrow"
            label = "Heading 3"

    class Heading4(StructBlock):
        heading = RichTextBlock(
            required=False,
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
            verbose_name="Heading 4",
            help_text="Enter a heading for the content.",
        )
        class Meta:
            icon = "pilcrow"
            label = "Heading 4"

    class Heading5(StructBlock):
        heading = RichTextBlock(
            required=False,
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
            verbose_name="Heading 5",
            help_text="Enter a heading for the content.",
        )
        class Meta:
            icon = "pilcrow"
            label = "Heading 5"

    class Paragraph(StructBlock):
        paragraph = RichTextBlock(
            required=False,
            features=[
                'emphasis',
                'bold',
                'italic',
                'link',
                'ul',
                'ol',
                'document-link',
                'code',
                'superscript',
                'subscript',
                'strikethrough',
            ],
            verbose_name="Paragraph",
            help_text="Enter content for this paragraph.",
        )
        class Meta:
            icon = "pilcrow"
            label = "Paragraph"

    content = StreamBlock(
        [
            ('heading1', Heading1()),
            ('heading2', Heading2()),
            ('heading3', Heading3()),
            ('heading4', Heading4()),
            ('heading5', Heading5()),
            ('paragraph', Paragraph()),
        ]
    )

    class Meta:
        template = "blocks/home/multi_level_content.html"
        icon = "pilcrow"
        label = "Multi Level Content"

class TwoColumnsHeadingSubHeadingContent(StructBlock):
    """Two columns, heading and subheading on the left, and a paragraph content on the right"""

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
        verbose_name="Heading",
        help_text="This text will be displayed in the heading section of this block.",
    )

    subheading = RichTextBlock(
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
        verbose_name="Subheading",
        help_text="This text will be displayed in the subheading section of this block.",
    )

    content = RichTextBlock(
        blank=True,
        null=True,
        verbose_name="Subheading",
        help_text="This text will be displayed in the content section of this block.",
    )

    class Meta:
        """ Meta TwoColumnsHeadingSubHeadingContent """
        template = "blocks/home/two_columns_heading_subheading_content.html"
        icon = "table-columns"
        label = "Two Column Content"


class TwoColumnsHeadingSubHeadingContentTwoButtons(TwoColumnsHeadingSubHeadingContent):
    primary_button_content = RichTextBlock(
        required=True,
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
        verbose_name="Primary button content",
        help_text="This text will be displayed in the primary button of this block.",
    )

    primary_button_link = PageChooserBlock(
        required=True,
        verbose_name="Button link",
    )

    secondary_button_content = RichTextBlock(
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
        verbose_name="Secondary button content",
        help_text="This text will be displayed in the secondary button of this block.",
    )

    secondary_button_link = PageChooserBlock(
        required=False,
        verbose_name="Button link",
    )

    class Meta:
        """ Meta TwoColumnsHeadingSubHeadingContentTwoButtons """
        template = "blocks/home/two_columns_heading_subheading_content_two_buttons.html"
        icon = "table-columns"
        label = "Two Column Content & Buttons"


class TwoColumnsHeadingSubheadingAccordion(TwoColumnsHeadingSubHeadingContent):
    """Two columns, heading and subheading on the left, and a set of accordions on the right"""

    class Accordion(StructBlock):
        title = RichTextBlock(
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
            verbose_name="Subheading",
            help_text="This text will be the title of this accordion card.",
        )

        content = RichTextBlock(
            blank=True,
            null=True,
            verbose_name="Subheading",
            help_text="This text will be the contents of this accordion block",
        )

        class Meta:
            template = ""
            icon = "pick"
            label = "Accordion Card"

    content = ListBlock(
        Accordion()
    )

    class Meta:
        template = "blocks/home/two_columns_heading_subheading_accordion.html"
        icon = "table-columns"
        label = "Two Column Accordion"


class FeatureSpotlight(TwoColumnsHeadingSubHeadingContent):
    """Heading and subheading at the top, and a list of feature cards"""

    class Feature(StructBlock):
        image = ImageChooserBlock(
            required=True,
            verbose_name="Image",
            help_text="This image will be displayed above the title of this feature card.",
        )
        title = RichTextBlock(
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
            verbose_name="Title",
            help_text="This text will be the title of this feature card.",
        )

        content = RichTextBlock(
            blank=True,
            null=True,
            verbose_name="Content",
            help_text="This text will be the contents of this feature block",
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
            icon = "pick"
            label = "Feature"

    content = ListBlock(
        Feature()
    )

    class Meta:
        template = "blocks/home/feature_spotlight.html"
        icon = "pick"
        label = "Feature Spotlight"


class CTACardLeftContentRightLargeImage(StructBlock):
    image = ImageChooserBlock(
        required=True,
        verbose_name="Image",
        help_text="This image will be displayed on the right-hand side of this card, the image will take up 3/5 of "
                  "the card.",
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
        verbose_name="Heading",
        help_text="This text will be the heading of this Call-to-action (CTA) card.",
    )

    content = RichTextBlock(
        blank=True,
        null=True,
        verbose_name="Content",
        help_text="This text will be the contents of this CTA card.",
    )

    button_text = CharBlock(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Button text",
        help_text="This text will be displayed inside the button in this card.",
    )

    button_page = PageChooserBlock(
        verbose_name="Button link",
        help_text="Choose a page to be opened when the user clicks the button in this card.",
    )

    class Meta:
        template = "blocks/home/cta_card_left_content_right_large_image.html"
        icon = "pick"
        label = "Call-to-action"


class CardCollection(StructBlock):
    class Card(StructBlock):
        image = ImageChooserBlock(
            required=True,
            verbose_name="Image",
            help_text="This image will be displayed as a background of the card.",
        )
        title = RichTextBlock(
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
            verbose_name="Title",
            help_text="This text will be the title of this card.",
        )
        content = RichTextBlock(
            blank=True,
            null=True,
            verbose_name="Content",
            help_text="This text will be the contents of this card",
        )
        card_page = PageChooserBlock(
            verbose_name="Page link",
            help_text="Choose a page to be opened when the user clicks this card.",
        )

        class Meta:
            icon = "pick"
            label = "Card"

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
        verbose_name="Heading",
        help_text="This text will be displayed in the heading section of this block.",
    )

    cards = ListBlock(
        Card()
    )

    class Meta:
        template = "blocks/home/card_collection.html"
        icon = "grip"
        label = "Card Collection"


class GalleryShowcase(StructBlock):

    class Image(StructBlock):
        image = ImageChooserBlock(
            required=True,
            verbose_name="Image",
            help_text="This image will be displayed above the title of this feature card.",
        )

        class Meta:
            icon = "image"
            label = "Image"

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
        verbose_name="Heading",
        help_text="This text will be displayed in the heading section of this block.",
    )

    subheading = RichTextBlock(
        blank=True,
        null=True,
        verbose_name="Subheading",
        help_text="This text will be displayed in the subheading section of this block.",
    )

    button_link = PageChooserBlock(
        required=False,
        verbose_name="Button link",
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

    gallery = ListBlock(
        Image()
    )

    class Meta:
        template = "blocks/home/gallery_showcase.html"
        icon = "image"
        label = "Gallery Showcase"


homepage_content_blocks = [
    ("homepage_headerandparagraph", HeaderAndParagraph()),
    ("homepage_multilevelcontent", MultiLevelContent()),
    ("homepage_twocolumnsheadingsubheadingcontent", TwoColumnsHeadingSubHeadingContent()),
    ("homepage_twocolumnsheadingsubheadingcontenttwobuttons", TwoColumnsHeadingSubHeadingContentTwoButtons()),
    ("homepage_twocolumnsheadingsubheadingaccordion", TwoColumnsHeadingSubheadingAccordion()),
    ("homepage_featurespotlight", FeatureSpotlight()),
    ("homepage_ctacardleftcontentrightlargeimage", CTACardLeftContentRightLargeImage()),
    ("homepage_cardcollection", CardCollection()),
    ("homepage_galleryshowcase", GalleryShowcase()),
]

homepage_content_streamfield = StreamField(
    homepage_content_blocks,
    null=True,
    blank=True,
    help_text="Choose blocks to be shown in the body."
)