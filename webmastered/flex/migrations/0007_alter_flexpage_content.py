# Generated by Django 4.0.5 on 2022-07-09 13:24

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0006_contactpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('homepage_headerandparagraph', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter a heading for the content.', required=False, verbose_name='Heading')), ('paragraphs', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('content', wagtail.blocks.RichTextBlock(features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter some content.', required=False, verbose_name='Content'))])))])), ('homepage_twocolumnsheadingsubheadingcontent', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the heading section of this block.', null=True, verbose_name='Heading')), ('subheading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the subheading section of this block.', null=True, verbose_name='Subheading')), ('content', wagtail.blocks.RichTextBlock(blank=True, help_text='This text will be displayed in the content section of this block.', null=True, verbose_name='Subheading'))])), ('homepage_twocolumnsheadingsubheadingcontenttwobuttons', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the heading section of this block.', null=True, verbose_name='Heading')), ('subheading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the subheading section of this block.', null=True, verbose_name='Subheading')), ('content', wagtail.blocks.RichTextBlock(blank=True, help_text='This text will be displayed in the content section of this block.', null=True, verbose_name='Subheading')), ('primary_button_content', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the primary button of this block.', null=True, verbose_name='Primary button content')), ('secondary_button_content', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the secondary button of this block.', null=True, verbose_name='Secondary button content'))])), ('homepage_twocolumnsheadingsubheadingaccordion', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the heading section of this block.', null=True, verbose_name='Heading')), ('subheading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the subheading section of this block.', null=True, verbose_name='Subheading')), ('content', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be the title of this accordion card.', null=True, verbose_name='Subheading')), ('content', wagtail.blocks.RichTextBlock(blank=True, help_text='This text will be the contents of this accordion block', null=True, verbose_name='Subheading'))])))])), ('homepage_featurespotlight', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the heading section of this block.', null=True, verbose_name='Heading')), ('subheading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be displayed in the subheading section of this block.', null=True, verbose_name='Subheading')), ('content', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='This image will be displayed above the title of this feature card.', required=True, verbose_name='Image')), ('title', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be the title of this feature card.', null=True, verbose_name='Title')), ('content', wagtail.blocks.RichTextBlock(blank=True, help_text='This text will be the contents of this feature block', null=True, verbose_name='Content'))])))])), ('homepage_ctacardleftcontentrightlargeimage', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='This image will be displayed on the right-hand side of this card, the image will take up 3/5 of the card.', required=True, verbose_name='Image')), ('heading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='This text will be the heading of this Call-to-action (CTA) card.', null=True, verbose_name='Heading')), ('content', wagtail.blocks.RichTextBlock(blank=True, help_text='This text will be the contents of this CTA card.', null=True, verbose_name='Content')), ('button_text', wagtail.blocks.CharBlock(blank=True, help_text='This text will be displayed inside the button in this card.', max_length=50, null=True, verbose_name='Button text')), ('button_page', wagtail.blocks.PageChooserBlock(help_text='Choose a page to be opened when the user clicks the button in this card.', verbose_name='Button link'))])), ('flexpage_pricing', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Give a heading for this pricing block', null=True, verbose_name='Table heading')), ('pricing_tables', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(blank=True, help_text='Give a name for this pricing table.', max_length=50, null=True, verbose_name='Table name')), ('heading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Give a heading for this pricing table', null=True, verbose_name='Table heading')), ('description', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Give a description for this pricing table', null=True, verbose_name='Table description')), ('tiers', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.RichTextBlock(blank=True, features=['superscript', 'subscript', 'strikethrough'], help_text='Enter the name of this tier.', null=True, verbose_name='Tier name')), ('price', wagtail.blocks.DecimalBlock(decimal_places=2, help_text='Enter the price p/m of this tier.', max_digits=6, min_value=0, required=True)), ('description', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Give a description for this pricing tier', null=True, verbose_name='Tier description')), ('highlight_tier_text', wagtail.blocks.CharBlock(blank=True, help_text="If you'd like to add a highlight to this tier, enter the highlight text here.", max_length=50, null=True, required=False, verbose_name='Highlight text')), ('features', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('feature_text', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Give a description of this feature, this will be displayed on the pricing table.', null=True, verbose_name='Feature text')), ('feature_type', wagtail.blocks.ChoiceBlock(choices=[('inc', 'Included'), ('add', 'Addition')], help_text="An icon will be added beside the feature description, when 'Included' is selected, a tick icon appears, when 'Addition' is selected, a plus icon appears. "))])))])))])))])), ('flexpage_frequentlyaskedquestions', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter a heading for this FAQ block.', null=True, verbose_name='Heading')), ('question_and_answer', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter a question.', null=True, verbose_name='Question')), ('answer', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter an answer to the question.', null=True, verbose_name='Answer'))])))])), ('flexpage_timeline', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter a heading for this timeline block.', null=True, verbose_name='Heading')), ('events', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(help_text='Give a name for this event.', max_length=50, required=False, verbose_name='Name')), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='This image will be displayed beside the event name, heading and content.', required=True, verbose_name='Image')), ('heading', wagtail.blocks.RichTextBlock(features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter a heading for this event.', required=True, verbose_name='Heading')), ('content', wagtail.blocks.RichTextBlock(blank=True, features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter content for this event.', null=True, verbose_name='Content')), ('button_content', wagtail.blocks.RichTextBlock(features=['emphasis', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Optional: You can add a button to display below the content. Enter the text to go inside the button', required=False, verbose_name='Button text')), ('button_link', wagtail.blocks.PageChooserBlock(help_text='Optional: You can link a page to this button.', required=False, verbose_name='Button link'))])))])), ('flexpage_stafflisting', wagtail.blocks.StructBlock([('heading', wagtail.blocks.RichTextBlock(features=['emphasis', 'bold', 'italic', 'link', 'document-link', 'code', 'superscript', 'subscript', 'strikethrough'], help_text='Enter a heading for this block.', required=True, verbose_name='Heading'))]))], blank=True, help_text='Choose blocks to be shown in the body.', null=True, use_json_field=None),
        ),
    ]
