# kills every job in the batch system (Oviedo)

import os
if 'cern.ch' in os.getcwd():
    os.system('bjobs > running.txt')
    text = open('running.txt')
    str = text.read()
    for line in str.splitlines():
        print  'bkill ' + line.split(' ')[0]
        os.system('bkill ' + line.split(' ')[0])

else:
    os.system('qstat > running.txt')
    text = open('running.txt')
    str = text.read()
    for line in str.splitlines():
        print 'qdel ' + line.split('.')[0]
        os.system('qdel ' + line.split('.')[0])
    


os.system('rm running.txt')
