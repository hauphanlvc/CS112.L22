import io,os,sys
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
f = open("Nhapdiem.txt","r")
# sys.stdout = open("OutNhapdiem.txt","w")
for i in f:
    print(type(i))