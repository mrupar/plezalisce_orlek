from django.shortcuts import render, get_object_or_404
from .models import Sector, Route

def home(request):
    routes_count = Route.objects.count()

    return render(request, 'climbing/index.html', {
        'routes_count': routes_count
    })

def routes_list(request):
    routes = Route.objects.select_related('sector').all()

    sector = request.GET.get('sector')
    grade = request.GET.get('grade')

    if sector and sector != "all":
        routes = routes.filter(sector__name=sector)

    if grade and grade != "all":
        routes = routes.filter(grade=grade)

    sectors = Sector.objects.all()

    return render(request, 'climbing/routes_list.html', {
        'routes': routes,
        'sectors': sectors,
        'selected_sector': sector,
        'selected_grade': grade,
    })

def route(request, id):
    route = get_object_or_404(Route, id=id)

    return render(request, 'climbing/route_detail.html', {
        'route': route
    })