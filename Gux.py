import re
import threading  
import time 
from time import sleep
import urllib.request
import sqlite3
import traceback
import json

class monitor():
    """WEB 页面后台监控类"""
    


    workInterval = 15  #工作间隔时间（分钟）
    starttime = time.time() #记录开始时间
    #mdb = MyDataBase()

    def __init__(self, **kwargs):
        
       
        print("monitor__init__")
        self.workInterval = self.workInterval * 60
        
        return super().__init__(**kwargs)
  


    def work(self):
        t1 = threading.Thread(target=self.task1)
        t1.setDaemon(True)
        t1.start()

  

    def task1(self):
        while True: 
            #mdb.execute("select * from task")
            #self.getUrl()

            

            sleep(self.workInterval)

    def getUrl(self,url):
        url = 'http://www.zrshop.com/'
        try: 
            response = urllib.request.urlopen(url)
            html = response.read().decode('utf-8')
            p = re.compile(r'<title>(?:(?!<\/title>)[\s\S])*<\/title>')
            re_h = re.compile('</?\w+[^>]*>')#HTML标签
            ret = p.findall(html)
            title = ""
            if(len(ret) > 0):
                 title = re_h.sub('',ret[0]) #去掉HTML 标签
            print(title)
        except Exception as e:
            print(e)
           
 


class MyDataBase():
    """数据库类"""
    cx = sqlite3.connect("DataBase/test.db")

    def __init__(self, **kwargs):
        return super().__init__(**kwargs)

    def initDatabase(self):
        cursor = self.cx.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='user';")

        if cursor.fetchone()[0] == 0:
            print("这是一个新的数据库")
            self.cx.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, username text, password text);")
            self.cx.execute("CREATE TABLE task (id INTEGER PRIMARY KEY, name text, url text, htmlTitle text,userid int);")
            self.cx.execute("CREATE TABLE taskLog (id INTEGER PRIMARY KEY, taskid int, resault int,userid int);")
            self.cx.execute("INSERT INTO user VALUES (1, 'admin','123123');")
            self.cx.commit()
    def executeNullReturn(self,sql):
        #self.cx.execute("INSERT INTO task VALUES (null, a, b, 1);")
        self.cx.execute(sql)
        self.cx.commit()
    def execute(self,sql):
        #self.cx.execute("INSERT INTO task VALUES (null, a, b, 1);")
        cur = self.cx.cursor()  
        cu = cur.execute(sql)  
        col_name_list = [tuple[0] for tuple in cur.description]  
       
        rs = cu.fetchall()
        result = {}
        result["head"]=col_name_list
        result["body"]=[]
        for row in rs:
            count=0
            resultLine={}
            for i in col_name_list:
                resultLine[col_name_list[count]]=row[count]
                count = count+1
            result["body"].append(resultLine)
        jsonString = []
        jsonString.append(result)
        return json.dumps(result,sort_keys=True,indent=4)
        #return result
            
            

    


    
