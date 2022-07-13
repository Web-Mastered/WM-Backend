# Generated by Django 4.0.6 on 2022-07-13 14:28

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_homepage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('homepage_headerandparagraph', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter a heading for the content.', required=False, verbose_name='Heading')), ('paragraphs', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock(features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter some content.', required=False, verbose_name='Content'))])))])), ('homepage_multilevelcontent', wagtail.blocks.StructBlock([('content', wagtail.blocks.StructBlock([('heading1', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter a heading for the content.', required=False, verbose_name='Heading 1'))])), ('heading2', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter a heading for the content.', required=False, verbose_name='Heading 2'))])), ('heading3', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter a heading for the content.', required=False, verbose_name='Heading 3'))])), ('heading4', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter a heading for the content.', required=False, verbose_name='Heading 4'))])), ('heading5', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter a heading for the content.', required=False, verbose_name='Heading 5'))])), ('heading6', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter a heading for the content.', required=False, verbose_name='Heading 6'))])), ('paragraph', wagtail.blocks.StructBlock([('paragraph', wagtail.blocks.RichTextBlock(features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter content for this paragraph.', required=False, verbose_name='Paragraph'))]))]))])), ('homepage_twocolumnsheadingsubheadingcontent', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the heading section of this block.', null=True, verbose_name='Heading')), ('subheading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the subheading section of this block.', null=True, verbose_name='Subheading')), ('content', wagtail.blocks.RichTextBlock(blank=True, help_text='This text will be displayed in the content section of this block.', null=True, verbose_name='Subheading'))])), ('homepage_twocolumnsheadingsubheadingcontenttwobuttons', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the heading section of this block.', null=True, verbose_name='Heading')), ('subheading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the subheading section of this block.', null=True, verbose_name='Subheading')), ('content', wagtail.blocks.RichTextBlock(blank=True, help_text='This text will be displayed in the content section of this block.', null=True, verbose_name='Subheading')), ('primary_button_content', wagtail.blocks.RichTextBlock(features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the primary button of this block.', required=True, verbose_name='Primary button content')), ('primary_button_link', wagtail.blocks.PageChooserBlock(required=True, verbose_name='Button link')), ('secondary_button_content', wagtail.blocks.RichTextBlock(features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the secondary button of this block.', required=False, verbose_name='Secondary button content')), ('secondary_button_link', wagtail.blocks.PageChooserBlock(required=False, verbose_name='Button link'))])), ('homepage_twocolumnsheadingsubheadingaccordion', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the heading section of this block.', null=True, verbose_name='Heading')), ('subheading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the subheading section of this block.', null=True, verbose_name='Subheading')), ('content', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be the title of this accordion card.', null=True, verbose_name='Subheading')), ('content', wagtail.blocks.RichTextBlock(blank=True, help_text='This text will be the contents of this accordion block', null=True, verbose_name='Subheading'))])))])), ('homepage_featurespotlight', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the heading section of this block.', null=True, verbose_name='Heading')), ('subheading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the subheading section of this block.', null=True, verbose_name='Subheading')), ('content', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='This image will be displayed above the title of this feature card.', required=True, verbose_name='Image')), ('title', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be the title of this feature card.', null=True, verbose_name='Title')), ('content', wagtail.blocks.RichTextBlock(blank=True, help_text='This text will be the contents of this feature block', null=True, verbose_name='Content'))])))])), ('homepage_ctacardleftcontentrightlargeimage', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='This image will be displayed on the right-hand side of this card, the image will take up 3/5 of the card.', required=True, verbose_name='Image')), ('heading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be the heading of this Call-to-action (CTA) card.', null=True, verbose_name='Heading')), ('content', wagtail.blocks.RichTextBlock(blank=True, help_text='This text will be the contents of this CTA card.', null=True, verbose_name='Content')), ('button_text', wagtail.blocks.CharBlock(blank=True, help_text='This text will be displayed inside the button in this card.', max_length=50, null=True, verbose_name='Button text')), ('button_page', wagtail.blocks.PageChooserBlock(help_text='Choose a page to be opened when the user clicks the button in this card.', verbose_name='Button link'))])), ('homepage_cardcollection', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the heading section of this block.', null=True, verbose_name='Heading')), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='This image will be displayed as a background of the card.', required=True, verbose_name='Image')), ('title', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be the title of this card.', null=True, verbose_name='Title')), ('content', wagtail.blocks.RichTextBlock(blank=True, help_text='This text will be the contents of this card', null=True, verbose_name='Content')), ('card_page', wagtail.blocks.PageChooserBlock(help_text='Choose a page to be opened when the user clicks this card.', verbose_name='Page link'))])))]))], blank=True, help_text='Choose blocks to be shown in the body.', null=True, use_json_field=None),
        ),
    ]
