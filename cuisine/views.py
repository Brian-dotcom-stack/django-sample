from django.shortcuts import render, get_object_or_404
from .models import Cuisine
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# cuisine_list view as a class
from django.views.generic import ListView, DetailView

class CuisineListView(ListView):
    queryset = Cuisine.objects.all()
    context_object_name = 'cuisines'
    paginate_by = 3
    template_name = 'cuisine/list.html'

# cuisine_detail view as a class

class CuisineDetailView(DetailView):
    model = Cuisine
    context_object_name = 'cuisine'
    template_name = 'cuisine/detail.html'

# Cuisine list view as a function
def Cuisine_list(request):
    """function to implement the logic of the list view for Cuisine"""

    object_list = Cuisine.objects.all()

    paginator = Paginator(object_list, 3)   # 3 posts in each page

    page = request.GET.get('page')

    try:
        cuisines = paginator.page(page)

    except PageNotAnInteger:   # if page is not an integer deliver the first page
        cuisines = paginator.page(1)

    except EmptyPage:   # if page is out of range deliver last page
        cuisines = paginator.page(paginator.num_pages)

    return render(
        request,
        'cuisine/list.html',
        {'page': page, 'cuisines': cuisines}
    )


# ---------------------------------------------------
# Cuisine_detail view as a function

def Cuisine_detail(request, cuisine):
    """function to implement the logic of the detail view for cuisine"""

    cuisineClicked = get_object_or_404(
        Cuisine,
        slug=cuisine,
        status='published'
    )

    return render(
        request,
        'cuisine/detail.html',
        {'cuisine': cuisineClicked}
    )
