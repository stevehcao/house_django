from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
