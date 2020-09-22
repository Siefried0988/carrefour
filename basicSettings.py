from selenium import webdriver
import time
import os



class RunJob:
    def __init__(self):

        self.number = 0

    def driverPath(self, url):
        driver = webdriver.Chrome(os.path.dirname(os.path.realpath(__file__)) + '.\\chromedriver.exe')
        driver.get(url)
        return driver   


    def endNotice(self):
        os.system(os.path.dirname(os.path.realpath(__file__)) + '//bell.mp3')

    def checkExecutionStatus(self, driver):
        time.sleep(3)
        completeJob = False
        while completeJob == False:
            resultOfExecution = driver.find_element_by_xpath("/html/body/div/div[2]/nav[2]/div[1]/div[1]/section[1]/section[2]/section/span/div/details/summary/span[1]/span[1]").get_attribute("data-execstate")
            print(resultOfExecution)
            if resultOfExecution == 'RUNNING':
                time.sleep(15)
            else:
                completeJob = True
        print('Job 已結束')
        self.endNotice()

    def executeJob(self, driver, nightShift = False):
        driver.implicitly_wait(20)
        driver.find_element_by_id('login').send_keys('admin')
        driver.find_element_by_id('password').send_keys('C4$ci_admin\n')
        time.sleep(3)
        driver.find_element_by_id('doReplaceFilters').click() 

        if nightShift == True:
            timestamp = time.strftime("%Y%m%d")
            driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/div[1]/form/div/div/section[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[2]/input').send_keys(timestamp)
            print(timestamp)
            

        #driver.find_element_by_id('execFormRunButton').click()
        #self.checkExecutionStatus(driver)



# windows = driver.window_handles
# driver.switch_to.window(windows[-1])
