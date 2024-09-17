import pymongo
from pymongo import MongoClient
from pymongo import ReturnDocument

global db
global cluster
global collection
def CnnMongo():
    cluster = MongoClient("mongodb+srv://kentQuaza:Wh7Y4sKJM4Gr4F0G@kentdevops.hmfhduv.mongodb.net/?retryWrites=true&w=majority&appName=KentDevOps")
    db = cluster["CodeDb"]
    collection = db["CodeRecord"]
    return db,collection
#Wh7Y4sKJM4Gr4F0G/kentQuaza
def insertDb(strDbName,name,lib,mean,syn,exp,type):
    cluster = MongoClient("mongodb+srv://kentQuaza:Wh7Y4sKJM4Gr4F0G@kentdevops.hmfhduv.mongodb.net/?retryWrites=true&w=majority&appName=KentDevOps")
    db = cluster["CodeDb"]
    #db,collection = CnnMongo()
    collect = db[strDbName]
    post = {"name":name,"lib":lib,"mean":mean,"syn":syn,"exp":exp,"type":type}
    collect.insert_one(post)
def showDb(strDbName):
    cluster = MongoClient("mongodb+srv://kentQuaza:Wh7Y4sKJM4Gr4F0G@kentdevops.hmfhduv.mongodb.net/?retryWrites=true&w=majority&appName=KentDevOps")
    db = cluster["CodeDb"]
    if checkExistCollection(strDbName) != "1":
        print("Table DB không tồn tại !")
        return 
    collection = db[strDbName]
    OrgListDb = collection.find()
    '''db,collection = CnnMongo()
    OrgListDb = db.collection.find()'''
    CvtListDb = list(OrgListDb)
    return CvtListDb
def showTableList():
    cluster = MongoClient("mongodb+srv://kentQuaza:Wh7Y4sKJM4Gr4F0G@kentdevops.hmfhduv.mongodb.net/?retryWrites=true&w=majority&appName=KentDevOps")
    db = cluster["CodeDb"]    
    collist = db.list_collection_names()
    print(collist)
    return collist
    '''for item in collist:
        print(item)'''
def addNewTable(strTableName):
    db,collection = CnnMongo()
    collection = db[strTableName]
    # check collection Name

    collist = db.list_collection_names()
    if strTableName in collist:
        print("DB table bị trùng !")
        return
    #db = cluster["CodeDb"]
    # Xac dinh so cot can them vao
    #print("---> Hãy Nhập Số Cột !")
    strIcolumn = input("---> Hãy Nhập Số Cột : ")
    strColumnName = ""
    if strIcolumn.isdigit() == False:
        print("---> Hãy Nhập Dạng Số !")
        return
    else:
        listColumn = list()
        dictPost = dict()
        for i in range(int(strIcolumn)):
            strColumnName = input(f"Hãy Nhập tên Cột số {i+1} : ")
            listColumn.append(strColumnName)
        for item in listColumn:
            dictPost[strColumnName] = "-"
    newTable = db[strTableName]
    #post = {"name":"-","lib":"-","mean":"-","syn":"-","exp":"-","type":"-"}
    newTable.insert_one(dictPost)    
    print("Add New Table Db Success !")
def checkExistName(strName,strType):
    db,collection = CnnMongo()
    result = collection.find({"name":strName,"type":strType})
    if result == None:
        result = []
    return list(result)
def checkExistCollection(strName):
    db,collection = CnnMongo()
    collist = db.list_collection_names()
    result = ""
    if strName in collist:
        result = "1"
    return result
def searchRecord():
    # yeu cau nhap Category va check
    cluster = MongoClient("mongodb+srv://kentQuaza:Wh7Y4sKJM4Gr4F0G@kentdevops.hmfhduv.mongodb.net/?retryWrites=true&w=majority&appName=KentDevOps")
    db = cluster["CodeDb"]   
    collection = db["category"]   
    collRecord = db["CodeRecord"]
    strCate = input("Mời Nhập Dạng Code Muốn Tra : ")
    myquery = { "name": strCate }
    mydoc = collection.find_one(myquery)
    if mydoc == None:
        print(f"Ma Code {strCate}nay khong ton tai!")
        return
    else:
        myquery = { "type": strCate }
        mydoc = collRecord.find(myquery)
    return list(mydoc)
def truyVanHaiDk(strName,strType):
    cluster = MongoClient("mongodb+srv://kentQuaza:Wh7Y4sKJM4Gr4F0G@kentdevops.hmfhduv.mongodb.net/?retryWrites=true&w=majority&appName=KentDevOps")
    db = cluster["CodeDb"] 
    collRecord = db["CodeRecord"]
    myquery = { "name": strName, "type": strType}
    mydoc = collRecord.find(myquery)
    a =list(mydoc)
    b=[]
    if a == None:
        print(f"Ma Code {strName} nay khong ton tai!")
        return b
    elif len(a)==0:
        print(f"Ma Code {strName} nay khong ton tai Trong Group {strType} !")
        return b
    else:
        return a 
def truyVanMotDk(strName):
    cluster = MongoClient("mongodb+srv://kentQuaza:Wh7Y4sKJM4Gr4F0G@kentdevops.hmfhduv.mongodb.net/?retryWrites=true&w=majority&appName=KentDevOps")
    db = cluster["CodeDb"] 
    collRecord = db["CodeRecord"]
    myquery = { "name": strName}
    mydoc = collRecord.find(myquery)
    a =list(mydoc)  
    b=[]  
    if a == None:
        print(f"Ma Code {strName} nay khong ton tai!")
        return b
    elif len(a)==0:
        print(f"Ma Code {strName} nay khong ton tai !!!")
        return b
    else:
        return a    
def updateData(strName,strLib,strMean,strSyn,strExp,type):
    cluster = MongoClient("mongodb+srv://kentQuaza:Wh7Y4sKJM4Gr4F0G@kentdevops.hmfhduv.mongodb.net/?retryWrites=true&w=majority&appName=KentDevOps")
    db = cluster["CodeDb"] 
    collRecord = db["CodeRecord"]
    #myquery = { "$and":{"name": strName,"type": type} }
    stringNew = str(type).strip()
    condition1 = {"name": strName}
    condition2 = {"type": stringNew}
    #timArr = collRecord.find_one({"$and": [condition1, condition2]})
    myquery = {"$and": [condition1, condition2]}
    newvalues = {"$set": {"lib": strLib,"mean": strMean,"syn": strSyn,"exp": strExp}}
    collRecord.find_one_and_update(myquery,newvalues,return_document = ReturnDocument.AFTER)
def deleleDcm(strName,type):
    cluster = MongoClient("mongodb+srv://kentQuaza:Wh7Y4sKJM4Gr4F0G@kentdevops.hmfhduv.mongodb.net/?retryWrites=true&w=majority&appName=KentDevOps")
    db = cluster["CodeDb"] 
    collRecord = db["CodeRecord"]
    #myquery = { "$and":{"name": strName,"type": type} }
    stringNew = str(type).strip()
    condition1 = {"name": strName}
    condition2 = {"type": stringNew}
    myquery = {"$and": [condition1, condition2]}
    collRecord.delete_one(myquery)
def truyVanByCodeGroup(strGroup):
    cluster = MongoClient("mongodb+srv://kentQuaza:Wh7Y4sKJM4Gr4F0G@kentdevops.hmfhduv.mongodb.net/?retryWrites=true&w=majority&appName=KentDevOps")
    db = cluster["CodeDb"] 
    collRecord = db["CodeRecord"] 
    myquery = {"type": strGroup}
    mydoc = collRecord.find(myquery)
    rs =list(mydoc)  
    b=[]  
    if rs == None:
        print(f"Ma Code {strGroup} nay khong ton tai!")
        return b
    elif len(rs)==0:
        print(f"Ma Code {strGroup} nay khong ton tai !!!")
        return b
    else:
        return rs         
def truyVanByText(strTxt,cbTxt):
    cluster = MongoClient("mongodb+srv://kentQuaza:Wh7Y4sKJM4Gr4F0G@kentdevops.hmfhduv.mongodb.net/?retryWrites=true&w=majority&appName=KentDevOps")
    db = cluster["CodeDb"] 
    collRecord = db["CodeRecord"] 
    myquery = {"$and":[{"name": {"$regex": strTxt, "$options": "i"}},{"type": cbTxt}]}
    mydoc = collRecord.find(myquery)
    rs =list(mydoc)  
    b=[]  
    if rs == None:
        print(f"Nội Dung {strTxt} Không Tồn Tại!")
        return b
    elif len(rs)==0:
        print(f"Nội Dung {strTxt} Không Tồn Tại !!!")
        return b
    else:
        return rs    
def truyVanByTextAll(strTxt):
    cluster = MongoClient("mongodb+srv://kentQuaza:Wh7Y4sKJM4Gr4F0G@kentdevops.hmfhduv.mongodb.net/?retryWrites=true&w=majority&appName=KentDevOps")
    db = cluster["CodeDb"] 
    collRecord = db["CodeRecord"] 
    myquery = {"name": {"$regex": strTxt, "$options": "i"}}
    mydoc = collRecord.find(myquery)
    rs =list(mydoc)  
    b=[]  
    if rs == None:
        print(f"Nội Dung {strTxt} Không Tồn Tại!")
        return b
    elif len(rs)==0:
        print(f"Nội Dung {strTxt} Không Tồn Tại !!!")
        return b
    else:
        return rs     