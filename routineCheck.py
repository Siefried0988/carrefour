from selenium import webdriver
import time
import os
from basicSettings import RunJob


rj = RunJob()

#check COD files status--TW
driver1 = rj.driverPath('https://support-rundeck-tw.carrefour.com/project/Daily_Monitor/job/show/08239748-f49f-4af0-ba05-201d2ad88500')
rj.executeJob(driver1)

#check COD jobs status
driver2 = rj.driverPath('https://support-rundeck-tw.carrefour.com/project/Daily_Monitor/job/show/8a0ee674-8024-4e8d-b1f8-9ee5a7182cf2')
rj.executeJob(driver2)



