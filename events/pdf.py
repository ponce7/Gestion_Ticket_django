from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 
from unittest import result

def html2pdf(template_path, context_dict={}):
    template = get_template(template_path)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("cp1252")), result)
    
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type="application/pdf")
    return None