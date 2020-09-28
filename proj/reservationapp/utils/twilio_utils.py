from twilio.rest import Client as TwilioClient
from twilio.base.exceptions import TwilioRestException
import logging
from django.conf import settings


logger = logging.getLogger(__name__)


TWILIO_CLIENT = TwilioClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


def send_response(to_number, message_text):
    client = TWILIO_CLIENT

    try:
        client.api.account.messages.create(
            to=to_number,
            from_=settings.TWILIO_NUMBER,
            body=message_text)

        logger.info('sending text - {}'.format(message_text))
        return {"success": True}
    except TwilioRestException as e:
        error_dict = {
            "success": False,
            "error": {
                "code": e.code,
                "status": e.status,
                "message": e.msg
            }
        }

        logger.warning('code: {} status: {} message: {}'.format(e.code, e.status, e.msg))
        return error_dict
