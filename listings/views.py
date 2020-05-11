from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices

# pulling in models
from .models import Listing


# Create your views here.
def index(request):
    # will fetch all listing from database
    # listings = Listing.objects.all()
    # fetch all listing by order
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # how to do pagination with django. 2nd params for how many we want to show
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {'listings': paged_listings}
    # can pass in 2nd params to pass to the view
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    # if something doesn't exist show 404 page
    # listing_id is coming from url 'listings/views.py
    # pk = primary key
    # get_object_or_404 is from django
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {'listing': listing}

    return render(request, 'listings/listing.html', context)


def search(request):
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
    }
    return render(request, 'listings/search.html', context)
