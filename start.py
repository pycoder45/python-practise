import pickle

a = [45,782,28,79,9]

#newFile = "newFile.pkl"
#openFile = open(newFile,"wb")

#pickle.dump(a,openFile)

#openFile.close()

newFile = "newFile.pkl"
openFile1 = open(newFile,"rb")
b = pickle.load(openFile1)
print(b)

aa = {
  "name" :  ["3rur","tjt","rjeje"],
  "numbers":  [3838,2828,689],
  "email" :  ["wei@fg","eit@fnn","wiri@xnc"]
}
fileone = open("file1.pkl","wb")
pickle.dump(aa,fileone)
fileone.close()

file2 = open("file1.pkl","rb")
print(pickle.load(file2)["name"])