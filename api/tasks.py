from celery.task import PeriodicTask
from datetime import timedelta
from api.data.hourly import hourly_data, validate_data


class CollectDataTask(PeriodicTask):
    run_every = timedelta(minutes=60)

    def run(self, **kwargs):
        validate_data(hourly_data())


@periodic_task(run_every=crontab(minute=0, hour='6,18'))