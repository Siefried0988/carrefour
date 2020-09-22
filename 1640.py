from selenium import webdriver
import time
import os
from basicSettings import RunJob


rj = RunJob()

#16:40及19:40都要執行
#1640 (TW) COD Check
driver = rj.driverPath('https://support-rundeck-tw.carrefour.com/project/Daily_Monitor/job/show/4f580479-26f1-4105-92d0-d44689e41c11')

rj.executeJob(driver)



