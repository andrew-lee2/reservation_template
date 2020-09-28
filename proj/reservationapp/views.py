from django.views.generic import View
from django.utils.decorators import method_decorator
import logging
from twilio.twiml.messaging_response import MessagingResponse
from django_twilio.decorators import twilio_view

from proj.reservationapp.tasks import revoke_celery_task
from proj.reservationapp.utils.text_parser import get_deletion_id


logger = logging.getLogger(__name__)


class ParseTextResponseView(View):

    @method_decorator(twilio_view)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        from_number = request.POST.get('From')
        text_body = request.POST.get('Body')

        if from_number and text_body:
            logger.info('Received the following text_body: {}'.format(text_body))
            deletion_id = get_deletion_id(text_body)
            if deletion_id:
                msg = revoke_celery_task(deletion_id)
            else:
                # Write a workflow to be executed here
                msg = ""
        else:
            msg = 'Missing from number or text_body'

        response = MessagingResponse()
        response.message(msg)
        logger.info('Sending the following message: {}'.format(msg))

        return response
