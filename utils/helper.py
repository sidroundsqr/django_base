"""Writing extra functions not related to any class but can be used in multiple classes"""

from django.utils.text import slugify


def get_unique_slug(model_instance, slug, slug_field_name):
    """
    Takes a model instance, sluggable field name (such as 'title') of that
    model as string, slug field name (such as 'slug') of the model as string;
    returns a unique slug as string.
    """
    unique_slug = slugify(slug)
    extension = 1
    model_class = model_instance.__class__

    while model_class._default_manager.filter( # pylint: disable=protected-access
            **{slug_field_name: unique_slug}
    ).exclude(pk=model_instance.id).exists():
        unique_slug = '{}-{}'.format(slug, extension)
        extension += 1

    return unique_slug
