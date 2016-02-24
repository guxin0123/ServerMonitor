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
        result = []

        for row in rs:
            resultlie={}
            count=0
            for i in col_name_list:
                resultlie["name"]=i
                resultlie["val"]=row[count]
                count = count+1
            result.append(resultlie)

        jsonString = []
        jsonString.append(result)
        return json.dumps(result,sort_keys=True,indent=4)
        #return result
            
            

    
    #================================
    def hasChild(appId):
        sql = "select count(*) from javahost_apptree where parentID=%d" % int(appId)
        cu.execute(sql)
        print("s")
        rs = cu.fetchone()
        return int(rs[0]) > 0
    """判断当前这个应用ID是不是叶节点"""
    def isleaf(appid):
        sql = "select count(*) from javahost_apptree where appID=%d and isleaf=1" % int(appid)
        cu.execute(sql)
        rs = cu.fetchone()
        return int(rs[0]) > 0
    """提取当前指定应用下面的全部的子节点。返回指定节点其下面的子节点列表
    [
        {
            id:1,
            text:33,
            value:01
            complete:true,
            hasChileren:true,
        }
    ]
    """
    def toJsonString(appId):
        resl = []
        sql = "select appID,appName,parentID,isLeaf from javahost_apptree where parentID=%d" % int(appId)
        cu.execute(sql)
        rs = cu.fetchall()
        for row in rs:
            result = {}
            result['complete'] = True
            if hasChild(row[0]):
                result['hasChildren'] = True
                result['ChildNodes'] = toJsonString(row[0])
            else:
                result['hasChildren'] = False
            result['id'] = row[0]
            result['text'] = row[1]
            if isleaf(row[0]):
                result['value'] = '0' + row[0]
            else:
                result['value'] = row[0]
            resl.append(result)
        return resl

    def generateInitTreeString():
        """获取根节点数据不断迭代生成树"""
        jsonString = []
        cu.execute('select appID,appName,parentID,isLeaf from javahost_apptree where parentID=0 and id!=1046')
        rs = cu.fetchall()
        for row in rs:
            result = {}
            result['complete'] = True
            if hasChild(row[0]):
                result['hasChildren'] = True
                result['ChildNodes'] = toJsonString(row[0])
            else:
                result['hasChildren'] = False
                result['ChildNodes'] = None
        
            result['id'] = row[0]
            result['text'] = row[1]
            if isleaf(row[0]):
                result['value'] = '0' + row[0]
            else:
                result['value'] = row[0]
            jsonString.append(result)
        return json.dumps(jsonString,ensure_ascii=True)
            


    
