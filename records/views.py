from django.http import HttpResponse
from .models import TextRecord

def add_record(request):
    # This creates a new entry in the database
    TextRecord.objects.create(content="This is a new record created at /add")
    return HttpResponse("<h1>Success!</h1><p>A new record has been added to the database.</p><a href='/show'>View all records</a>")

def show_records(request):
    # This pulls all entries from the database
    all_items = TextRecord.objects.all()
    response_html = "<h1>Database Records:</h1><ul>"
    for item in all_items:
        response_html += f"<li>{item.content} (Saved at: {item.created_at})</li>"
    response_html += "</ul><br><a href='/add'>Add another record</a>"
    return HttpResponse(response_html)