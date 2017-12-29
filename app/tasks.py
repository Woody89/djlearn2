from __future__ import absolute_import, unicode_literals
import logging
from celery.app import shared_task
from django.core.mail import send_mail


logger = logging.getLogger(__name__)

@shared_task
def celery_send_email(subject, message, from_email, recipient_list, **kwrags):
    try:
        print "hell"
#         send_mail(subject, message, from_email, recipient_list, **kwrags)
        return 'success!'
    except Exception as e:
        logger.error("Send failed: {}".format(e))