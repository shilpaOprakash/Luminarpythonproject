f=open("covid_19_india(1).csv","r")
dict={}

for lines in f:
    data=lines.rstrip("\n").split(",")
    print(data)
    state=data[3]
    confirmed=int(data[-1])
    dict[state]=confirmed
for k,v in dict.items():
    print(k,"=>",v)

data=max(dict,key=dict.get)
print(data,dict[data])
