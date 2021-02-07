import requests
from django.conf import settings
from django.views.generic import TemplateView


class MainTemplateView(TemplateView):
    template_name = 'main/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quote'] = self.get_quote()
        return context

    @staticmethod
    def get_quote() -> dict or bool:
        """
        Request to the API and parsed the response to return the title and content
        :return:
        """
        url = settings.QUOTE_API_PROVIDER

        response = requests.get(url)
        formatted = response.json()

        if response.status_code == 200:
            author = formatted[0]['title']['rendered']
            content = formatted[0]['content']['rendered']

            return {'author': author, 'content': content}

        return False