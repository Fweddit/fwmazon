from django.shortcuts import render_to_response
from django.template import RequestContext
from checkout.models import ShippingDestination
def options(req):
    destinations = ShippingDestination.objects.filter(active=True)
    return render_to_response('checkout/options.html', {'destinations': destinations}, context_instance=RequestContext(req))