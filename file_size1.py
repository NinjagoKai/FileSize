import os, sys, scandir,pandas as pd, threading
#todo conversion to human readalbe numbers
#todo selection of folder by user
#todo total size of folder
def folder_size(path='.'):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += folder_size(entry.path)
    return total
#sys.setrecursionlimit(20000)
def checkfile(path):
    if os.path.isfile(path):
        os.remove(path)
    open(path, 'w').close()

def list_of_files1(r,output_file):
#r='//'
    print ("Opcja 1 wszystkie foldery rowniez zagniezdone")
    root=r
    print(root)
    data=[]
    for root, dirs, files in os.walk(root):
        try:
            for d in dirs:
                t=[]
                path = os.path.join(root, d)
                typ="dir"
                size=folder_size(path)
                print("Folder Size info: " + path + " " + str(size))
                t = [typ, path, size]
                data.append(t)
            for f in files:
                t=[]
                path = os.path.join(root, f)
                typ = "file"
                size = os.path.getsize(path)
                print("Folder Size info: " + path + " " + str(size))
                t = [typ, path, size]
                data.append(t)
            # print (os.path.join(root, d))
        except OSError:
            print(OSError.errno)
            typ = OSError.errno
            size = 0
            t = [typ, path, size]
            data.append(t)
    df=pd.DataFrame(data,columns=['type','path','size'])
    df.to_csv(output_file,sep=";",header= False, mode='a')


#list_of_files1('//home/','data.csv')


w1='//'
output='//home/m/Documents/Python/FileSize/output1.csv'
checkfile(output)
#os.remove(output)
#data=[]
#df=pd.DataFrame(data,columns=['type','path','size'])

for ob in os.listdir(w1):
    threadingObj=threading.Thread(target=list_of_files1, args=(os.path.join(w1,ob),output))
    threadingObj.start()

