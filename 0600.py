from selenium import webdriver
import time
import os
from basicSettings import RunJob


rj = RunJob()

#Update Job History to Central DB
driver1 = rj.driverPath('https://support-rundeck-tw.carrefour.com/project/Daily_Monitor/job/show/3bfd8b64-49cf-446f-8ca2-095696ccbe3e')
rj.executeJob(driver1)

#Update Job History - Integrate and Extract Report
driver2 = rj.driverPath('https://support-rundeck-tw.carrefour.com/project/Daily_Monitor/job/show/ecd3ab85-875a-447c-87a6-e736a105cd1b')
rj.executeJob(driver2, nightShift = True)



