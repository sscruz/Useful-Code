# kills every job in the batch system (Oviedo)

import os
os.system('qstat > running.txt')
text = open('running.txt')
str = text.read()
for line in str.splitlines():
    print 'qdel ' + line.split('.')[0]
    os.system('qdel ' + line.split('.')[0])
os.system('rm running.txt')
