def Loe_failist(fail:str)->list:
    f=open(fail,"r", encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend

loetelu=Loe_failist("Loetelu.txt")
print(loetelu)
def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,'w',encoding="utf-8-sig")
    for line in jarjend:
        f.write(line+'\n')
    f.close()

loetelu=Loe_failist("Loetelu.txt")
print(loetelu)
for i in range(8,11,1):
    loetelu.append(input(f"{i}-i: "))
Kirjuta_failisse("Loetelu.txt", loetelu)
loetelu=Loe_failist("Loetelu.txt")
print(loetelu)
