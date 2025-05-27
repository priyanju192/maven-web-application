import csv

f = open('/var/jenkins_home/reports/trivy-report.json')
data = json.load(f)
f.close()

new_data = []

for i in data:
   flat = {}
   names = i.keys()
   for n in names:
      try:
         if len(i[n].keys()) > 0:
            for ii in i[n].keys():
               flat[n+"_"+ii] = i[n][ii]
      except:
         flat[n] = i[n]
   new_data.append(flat)  

f = open(filename, "r")
writer = csv.DictWriter(f, new_data[0].keys())
writer.writeheader()
for row in new_data:
   writer.writerow(row)
f.close()
