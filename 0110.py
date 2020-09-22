from selenium import webdriver
import time
import os
from basicSettings import RunJob

rj = RunJob()

#PCM-14834 TW Check POSinbound import data status
driver = rj.driverPath('https://support-rundeck-tw.carrefour.com/project/Daily_Monitor/job/show/305ff9ef-6c43-4504-a35e-24c0770d9ce5')

rj.executeJob(driver)



