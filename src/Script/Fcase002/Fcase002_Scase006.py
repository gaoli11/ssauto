# -*- coding: cp936 -*-
import os
import sys
os.chdir("..\..")
sys.path.append("C:\workspace\FossAutoTest")

from ModulePackage.Module import * 

class Test(unittest.TestCase):
    global logger
    global judge
    global GetHandOverBillNo
    global TaskCode
    global driver
    logging.config.fileConfig(r"./conf/msg.conf")
    logger = logging.getLogger("FOSS")
    
    def setUp(self):
        self.logger=logger
        self.logger.info("启动测试......")
        self.boolean=True
        self.browser = webdriver.Remote('http://192.168.20.23:8100/wd/hub', DesiredCapabilities.CHROME);
        #self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)
        self.browser.set_window_size(1280,700)
        self.browser.set_window_position(0,0)
    
    def tearDown(self):
        time.sleep(10)
        self.browser.quit()
    
    
    def testFoss_Fcase002(self):
        GetReturn=""
        try:
            
            Login(self,"http://192.168.10.50/stl-web/login/index.action","129394","qqqqqq","上海空运总调")
            Navigation(self,"卸车管理-查询卸车任务")
            GetReturn=NewUnloadTask(self,"",self.GetReturnValue(20,9),"黄圣铭")
        except:
            self.boolean=False
            raise RuntimeError
        finally:
            if self.boolean==True:
                self.WriteRes(25, 8, "True!")
            else:
                self.WriteRes(25, 8, 'FALSE!')
            if GetReturn !="":
                self.WriteRes(25,9,GetReturn)
            Path=".\ResultPic"+"\\"+datetime.datetime.now().strftime('%Y_%m_%d')
            try:
                os.mkdir(Path)
            except:
                pass
            Path=Path+"\\Fcase002"
            Local = Path+"\\Scase006"+"-"+datetime.datetime.now().strftime('%Y_%m_%d %H_%M_%S')+".jpg"
            try:
                os.mkdir(Path)
            except:
                pass
            self.browser.save_screenshot(Local)
            
    def GetReturnValue(self,nrow,ncol):
        data = xlrd.open_workbook(".\TestCase\TestCase.xls")
        case = data.sheet_by_name("test case")
        nrows=case.nrows
        return case.row_values(nrow)[ncol]
    
    def WriteRes(self,nrow,ncol,input):
        rb = open_workbook('.\TestCase\TestCase.xls')
        rs = rb.sheet_by_index(0) 
        wb = copyd(rb)
        ws = wb.get_sheet(0)
        ws.write(nrow, ncol, input)
        wb.save('.\TestCase\TestCase.xls')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
