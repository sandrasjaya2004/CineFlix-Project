from apscheduler.schedulers.background import BackgroundScheduler

from django.utils import timezone

from subscriptions.models import UserSubscriptions

# def print_hello():

#     print('hello world')

def disable_subscription():

    current_date_time=timezone.now()

    UserSubscriptions.objects.filter(active=True,end_date_lte=current_date_time).update(active=False)

def scheduler_job():

    scheduler=BackgroundScheduler()

    scheduler.add_job(disable_subscription,'cron',minute=1,hour=0)

    scheduler.start()
