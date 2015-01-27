from django.shortcuts import render
import logging
# Create your views here.
logger = logging.getLogger("holyshit")


def index_view(request):
    return render(request, 'reddit/index.html')