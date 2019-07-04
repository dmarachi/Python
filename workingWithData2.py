# importing csv module 
import csv

# csv file name and open it to read
Data = open("Census_by_Community_2018.csv")
fileReader = csv.reader(Data)

headerList = next(fileReader)
counter = 0
# dataArray = []
dictionary={}
dictionary2={}

with open("report.txt", "w") as file:
    for row in fileReader:

        # print(headerList[0], row[0])
        # print(headerList[4], row[4])
        # print(headerList[9], row[9])
        # dataArray.append(row)
        # dictionary[row[0]] = row[4]
        # dictionary[] = row[4]
        counter += 1
        if row[0] in dictionary.keys():
        	dictionary[row[0]] += int(row[9])
        else:
        	dictionary[row[0]] = int(row[9])
   
        if row[4] in dictionary2.keys():
        	dictionary2[row[4]] += int(row[9])
        else:
        	dictionary2[row[4]] = int(row[9])
    print(dictionary2)
    print(dictionary)

    file.write("This is the report test data")
    file.write("Data " + str(counter) + " ---> " + str(dictionary) + "\n")
    file.write("Total: " + str(counter))