from config import celery_app
from celery_once import QueueOnce
import logging


logger = logging.getLogger(__name__)


@celery_app.task(base=QueueOnce)
def example_task(x, y):
    return x + y


def revoke_celery_task(task_id):
    celery_app.control.revoke(task_id, terminate=True)
    revoke_msg = f'Revoked for task id {task_id}'
    logger.info(revoke_msg)
    return revoke_msg
