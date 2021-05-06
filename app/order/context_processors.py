"""context processor objects
    """
from order.initial_order_data_context_manager import (
    InitialOrderDataContextManager)


def initial_order(request):
    return {'initial_order': InitialOrderDataContextManager(request)}
