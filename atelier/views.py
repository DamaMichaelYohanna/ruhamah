from django.shortcuts import render

LOOKS = [
    {"image": "/static/atelier/images/african-heritage.jpg", "caption": "A STUDY IN PRINT · 01", "alt": "Juliet wearing a pink and white patterned dress", "size": "look-tall"},
    {"image": "/static/atelier/images/red-evening-look.jpg", "caption": "A STUDY IN FORM · 02", "alt": "Juliet in a red evening dress", "size": "look-short"},
    {"image": "/static/atelier/images/white-contemporary-look.jpg", "caption": "CONTEMPORARY WEAR · 03", "alt": "Juliet wearing a white and blush contemporary outfit", "size": "look-mid"},
    {"image": "/static/atelier/images/african-heritage.jpg", "caption": "AFRICAN HERITAGE · 04", "alt": "Juliet wearing a pink and white patterned dress", "size": "look-tall"},
    {"image": "/static/atelier/images/black-suit-portrait.png", "caption": "THE CORPORATE EDIT · 05", "alt": "Juliet in a tailored black suit on a rooftop walkway", "size": "look-tall"},
    {"image": "/static/atelier/images/black-suit-city-view.png", "caption": "A MOMENT ABOVE THE CITY · 06", "alt": "Juliet in a black suit overlooking the city", "size": "look-mid"},
    {"image": "/static/atelier/images/black-suit-rooftop-walk.png", "caption": "THE CORPORATE EDIT · 07", "alt": "Juliet walking in a black suit on a rooftop", "size": "look-short"},
]


def home(request):
    return render(request, "atelier/home.html", {"looks": LOOKS})


def collections(request):
    return render(request, "atelier/collections.html")


def story(request):
    return render(request, "atelier/story.html")


def lookbook(request):
    return render(request, "atelier/lookbook.html", {"looks": LOOKS})


def bespoke(request):
    return render(request, "atelier/bespoke.html")


def contact(request):
    return render(request, "atelier/contact.html")
