# run adder.sh (friendtree merging) for all the samples in a given directory
# adder.sh should be located in ../. 

import os
chunks = os.listdir('.')
samples = []
for chunk in chunks:
    if 'chunk0' in chunk: os.system('bash ../adder.sh %s'%chunk.replace('evVarFriend_','').replace('.chunk0.root',''))
    if 'chunk0' in chunk: print 'bash ../adder.sh %s'%chunk.replace('evVarFriend_','').replace('.chunk0.root','')
