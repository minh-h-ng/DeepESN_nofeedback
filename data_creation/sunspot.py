import csv

dataFile = '/home/minh/PycharmProjects/DeepESN/data_creation/SN_ms_tot_V2.0.csv'
writeFile = '/home/minh/PycharmProjects/DeepESN/data_backup/Sunspots'

with open(dataFile,'r') as f:
    reader = csv.reader(f)
    toWrite = []
    for line in reader:
        data = line[0].split(';')
        #print('data:',float(data[3]))
        if (float(data[3])>=0):
            toWrite.append(float(data[3]))
    print('toWrite:',toWrite)

with open(writeFile,'w') as f:
    for i in range(len(toWrite)-1):
        f.write(str(toWrite[i]) + ',' + str(toWrite[i+1]) + '\n')


