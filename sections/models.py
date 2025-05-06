from django.db import models
from django.template.defaultfilters import title
from django.utils.translation import gettext_lazy as _
from users.models import NULLABLE


class Section(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'), **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name =_('Section')
        verbose_name_plural =_('Sections')
        ordering = ['id']

class Content(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name=_('Section'))
    title = models.CharField(max_length=150,verbose_name=_("Title"))
    content = models.CharField(verbose_name=("Content"))

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _('Section Content')
        verbose_name_plural = _("Section Contents")
        ordering = ['id']