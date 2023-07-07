#after celery.py file written completed

from celery import shared_task


@shared_task(bind=True)
def test_func(self):
    #operation perform
    for i in range(10):
        print(i)
    return 'done'
