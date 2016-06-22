import os

job_name = os.environ[JOB_NAME]
Status = os.environ[EXECUTOR_NUMBER]
print "Yogesh"
print "Job Name: " + job_name
print "Job Status: " + Status
