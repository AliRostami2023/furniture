from django.db import models
from django.utils.translation import gettext_lazy as _


class CreateMixin(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('تاریخ ایجاد'))

    class Meta:
        abstract = True

        
class UpdateMixin(models.Model):
    update_at = models.DateTimeField(auto_now_add=True, verbose_name=_('تاریخ آپدیت'))

    class Meta:
        abstract = True

class Image(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name=_('تصویر'))

    class Meta:
        verbose_name = _('تصویر')
        verbose_name_plural = _('تصاویر')

