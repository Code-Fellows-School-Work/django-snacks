from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snacks"] = [
            {
                "title": "Baklava",
                "description": "A rich, sweet dessert pastry made of layers of filo filled with chopped nuts and sweetened with syrup or honey.",
                "reference_url": "https://en.wikipedia.org/wiki/Baklava"
            }, {
                "title": "Macaron",
                "description": "A sweet meringue-based confection made with egg white, icing sugar, granulated sugar, almond meal, and food coloring.",
                "reference_url": "https://en.wikipedia.org/wiki/Macaron"
            }, {
                "title": "Samosa",
                "description": "A fried or baked pastry with a savory filling, such as spiced potatoes, onions, peas, cheese, beef, or other meats.",
                "reference_url": "https://en.wikipedia.org/wiki/Samosa"
            },
        ]


        return context

class AboutPageView(TemplateView):
    template_name = 'about.html'