from django.http import HttpResponse
from datetime import datetime
from django.utils import timezone


def index(request):
    return HttpResponse(f"naive {datetime.now()} aware {timezone.now()}Hello, world. You're at the polls index.")
