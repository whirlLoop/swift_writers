from django.conf import settings


class InitialOrderDataContextManager(object):

    def __init__(self, request):
        self.session = request.session
        initial_order_data = self.session.get(settings.INITIAL_ORDER_DATA_ID)
        if not initial_order_data:
            initial_order_data = self.session[settings.INITIAL_ORDER_DATA_ID] = {
            }
        self.initial_order_data = initial_order_data

    def set_initial_order_data_to_context(self, initial_data):
        """Set order items to context

        Args:
            initial_data (dict): a dict containing the data to be set
        """
        order_owner = initial_data['email']
        self.initial_order_data[order_owner] = {}
        for key, value in initial_data.items():
            self.initial_order_data[order_owner][key] = str(value)
        self.save_session()

    def save_session(self):
        """Mark the session as "modified" to make sure it gets saved (by django)
        """
        self.session.modified = True

    def remove_data_from_session(self):
        """Remove data from session
        """
        del self.session[settings.INITIAL_ORDER_DATA_ID]
        self.save_session()
