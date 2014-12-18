import csv
import sys

line="\n"
data=[]
f=open("../data/movies.txt")
item=()
csvfile = file('result/csv_test.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['productid','userid','name','helpfulness','score','time','summary','text'])

for i in range(0, 100000):
	line=f.readline()

	if (line=="\n"):
		writer.writerow(item)
		item=()

	else:
		line=line.split(":")[1]
		item= item+(line,)

    # if (line=="\n"):
    # 	csvfile = file('data.csv', 'w+')
    #     writer = csv.writer(csvfile)
    #     writer.writerow(data)
    #     csvfile.close()
    # else:
    #     line=f.readline()
    #     data.append(line)  

