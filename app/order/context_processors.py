"""context processor objects
    """
from order.domain_objects.initial_order import InitialOrder


def initial_order(request):
    return {'initial_order': InitialOrder}
