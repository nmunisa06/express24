from django.db.models import Model, CharField, SlugField
from django.template.defaultfilters import slugify


class SlugBaseModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args,**kwargs):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
