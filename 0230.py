from selenium import webdriver
import time
import os
from basicSettings import RunJob


rj = RunJob()

#check EOD2 finish or not--TW
driver = rj.driverPath('https://support-rundeck-tw.carrefour.com/project/Daily_Monitor/job/show/6dab64a4-548f-4442-af8e-e504bf043b23')

rj.executeJob(driver)

