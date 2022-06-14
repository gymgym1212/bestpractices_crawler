from cmath import log
import os

logfile = open('./log','w')

cmd = '~/go/bin/scorecard-darwin-amd64 --repo=github.com/mbtproject/mbt'
res = os.popen(cmd)
output = res.read()
idx = output.find('Aggregate score: ') + len('Aggregate score: ')
score = 0
flag = 1
while output[idx] != '/':
    if output[idx] == ' ':
        idx+=1
        continue

    if output[idx] != '.':
        score = score * 10 + int(output[idx])
    else:
        flag = 10
    idx+=1

score = score / flag
logfile.write(str(score))
logfile.close()