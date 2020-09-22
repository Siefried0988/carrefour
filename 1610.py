from selenium import webdriver
import time
import os
from basicSettings import RunJob

rj = RunJob()

#跑完需發訊息 PCM-13859 Over Return daily scan, No store with issue data.
#PCM-13859_Over_Return__Scan
driver = rj.driverPath('https://support-rundeck-tw.carrefour.com/project/Daily_Monitor/job/show/da88888f-8c36-4b26-9594-1337b368f7d4')

rj.executeJob(driver)