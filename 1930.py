from selenium import webdriver
import time
import os
from basicSettings import RunJob


rj = RunJob()

#00新增：Check COD_G2-3 Files_check
driver = rj.driverPath('https://support-rundeck-tw.carrefour.com/project/Daily_Monitor/job/show/6c26ae5f-89ed-455b-9f78-0fafa1baeef7')

rj.executeJob(driver)

