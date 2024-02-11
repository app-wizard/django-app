from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request,) -> HttpResponse:

    context = {
        "title": "Home - main",
        "content": "Step into a world where every bite tells a story of centuries-old traditions",
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "about",
        "content": "About page",
        "text_on_page": "Welcome to Lotus Pavilion, where the spirit of traditional Chinese cuisine is reimagined with modern elegance. Nestled in the vibrant cityscape of Azure Bay, Lotus Pavilion stands as a beacon of culinary innovation and heritage. Chef Ming Zhao, our visionary founder, embarked on a quest to blend the rich flavors of his Chinese roots with contemporary culinary techniques. His journey, fueled by the diverse tastes of China's regions, led to the creation of a unique dining experience that honors the past while embracing the future. At Lotus Pavilion, our menu is a celebration of contrast and harmony. From the delicate balance of Cantonese dim sum to the fiery zest of Sichuan dishes, our chefs expertly craft each meal using fresh, locally-sourced ingredients, ensuring a symphony of flavors in every bite. The restaurant's ambiance reflects a fusion of tradition and modernity, providing a warm, welcoming space for guests to explore the wonders of Chinese cuisine. Lotus Pavilion is not just a place to eat; it's a destination where culinary dreams come to life, offering a memorable journey through the heart of Chinese gastronomy. Join us at Lotus Pavilion, where every meal is a masterpiece, and every visit is an adventure in flavor.",
    }
    return render(request, "main/about.html", context)
