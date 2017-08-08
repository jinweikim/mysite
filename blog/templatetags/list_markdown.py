from django import template
from django.conf import settings
import markdown2
import markdown
register = template.Library()

@register.filter(name='mark')
@register.simple_tag()
def mark(value):
    value = markdown.markdown(value,extras=["code-friendly","fenced-code-blocks","header-ids","tocs","metadata"])
    return value

def markdown_to_html(markdowntext,images):
    # md = markdown2.Markdown()
    image_ref = ""
    for image in images:
        image_url = settings.MEDIA_URL + image.image.url
        image_ref = "%s\n[%s]: %s" % (image_ref,image,image_url)

    md = "%s\n%s" % (markdowntext,image_ref)
    html = markdown2.Markdown(md)
    return html

@register.filter(name='body_html')
@register.simple_tag()
def body_html(value):
    return markdown_to_html(value.content,value.images.all())

