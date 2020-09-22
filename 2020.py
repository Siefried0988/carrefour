from selenium import webdriver
import time
import os
from basicSettings import RunJob


rj = RunJob()

#2000 (TW) COD Check dly fils are arrived at CM+
driver1 = rj.driverPath('https://support-rundeck-tw.carrefour.com/project/Daily_Monitor/job/show/063ed7c2-fc38-432a-9218-6a68ddd573f7')
rj.executeJob(driver1)

#check EXD files arrived to stores--TW
driver2 = rj.driverPath('https://support-rundeck-tw.carrefour.com/project/Daily_Monitor/job/show/e8004393-6c45-4669-a01c-d216236bce3b')
rj.executeJob(driver2)



