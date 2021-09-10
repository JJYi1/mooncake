from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from main import chechkmooncake

# BlockingScheduler: use when the scheduler is the only thing running in your process
scheduler = BlockingScheduler()

# Schedules the job_function to be executed Monday through Friday at between 12-16 at specific times.
scheduler.add_job(chechkmooncake, 'cron', day_of_week='mon-sun', hour='7-23', minute='5,15,25,35,45,57', start_date='2021-08-26 12:00:00', timezone=None)

# Start the scheduler
scheduler.start()
