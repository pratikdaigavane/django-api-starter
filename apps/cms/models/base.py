from django.db import models
from django.utils.text import slugify


class AbstractMetadata(models.Model):
    OG_TYPES = (
        ('video.other', 'Video'),
        ('video.movie', 'Movie'),
        ('video.tv_show', 'TV Show'),
        ('article', 'Article'),
        ('book', 'Book'),
        ('profile', 'Profile'),
        ('website', 'Website'),
    )

    meta_title = models.CharField('<meta> title', max_length=80, blank=True, null=True)
    meta_description = models.CharField('<meta> description', max_length=160, blank=True, null=True)
    og_title = models.CharField(' og:title', max_length=80, blank=True, null=True)
    og_type = models.CharField(' og:type', choices=OG_TYPES, default='website', max_length=30)
    og_description = models.CharField(' og:description', max_length=200, blank=True, null=True)

    class Meta:
        abstract = True


class SlugBase(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=140, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Page.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)


class AbstractContentType(SlugBase):
    tags = models.ManyToManyField('cms.Tag', related_name='tags')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
