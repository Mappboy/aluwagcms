from django.contrib.gis.db import models

# Create your models here.
from django.contrib.gis.forms import OSMWidget
from wagtail.api import APIField
from wagtail.core.models import Page

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

# Divide into country
# ALUCountry


class CountryPage(Page):
    name = models.CharField(max_length=40)
    geom = models.PolygonField()

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('geom', widget=OSMWidget)
    ]

    api_fields = [
        APIField('name'),
        APIField('geom'),
    ]