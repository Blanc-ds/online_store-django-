from django.db.models import Q

from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=(query))

    keywords = [word for word in query.split()]

    q_objects = Q()

    for kw in keywords:
        q_objects |= Q(description__icontains=kw)
        q_objects |= Q(name__icontains=kw)

    return Products.objects.filter(q_objects)