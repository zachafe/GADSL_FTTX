mascara = "255.255.128.0"
anillo = "6"
base = "10.66."

for i in range(14,40):
    for j in range (0,256):
        ip = base+str(i)+"."+str(j)
        #print(ip)
        print("(3,'{}',{},{},2,664,now()),".format(
            ip,mascara,anillo
        ))