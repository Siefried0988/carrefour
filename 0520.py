from selenium import webdriver
import time
import os
from basicSettings import RunJob


rj = RunJob()

#check SOD finish or not--TW
driver = rj.driverPath('https://support-rundeck-tw.carrefour.com/project/Daily_Monitor/job/show/ddae1ca7-5969-4e9b-be4d-6f77e2903465')

rj.executeJob(driver)


