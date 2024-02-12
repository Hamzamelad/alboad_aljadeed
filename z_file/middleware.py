# myapp/middleware.py

from django.http import HttpResponseNotFound
from django.conf import settings
import os

class ReactAppMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the response is a 404 Page Not Found error
        if response.status_code == 404:
            # Get the path to the index.html file in your React app
            index_path = os.path.join(settings.REACT_APP_DIR, 'index.html')

            # Serve the index.html file for all unmatched paths
            with open(index_path, 'r') as f:
                return HttpResponseNotFound(f.read())

        return response
