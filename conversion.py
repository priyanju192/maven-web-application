import json
import csv

with open("/var/jenkins_home/reports/trivy-report.json") as file:
    data = json.load(file)



# create the csv writer object
pt_data1 = open('pt_data1.csv', 'w')
csvwriter = csv.writer(pt_data1)

count = 0

for pt in data:

      if count == 0:

             header = pt.keys()

             csvwriter.writerow(header)

             count += 1

      csvwriter.writerow(pt.values())

pt_data1.close()
