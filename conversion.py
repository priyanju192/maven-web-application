import json
import csv

with open('/var/jenkins_home/reports/trivy-report.json') as jf:
    jd = json.load(jf)

df = open('/var/jenkins_home/reports/rep-jsonoutput.csv', 'w', newline='')
cw = csv.writer(df)

c = 0
for data in jd:
    if c == 0:
        header = data.keys()
        cw.writerow(header)
        c += 1
    cw.writerow(data.values())

df.close()
