import os 
import re

debug = False
from multiprocessing import Pool

def runIt(cmd):
    if debug: print cmd
    else: os.system(cmd) 

def makeTheThing(ls):
    if ls == 'updated_cards': return
    os.mkdir('updated_cards/%s'%ls)
    result = re.findall(r"_[0-9]+",ls)
    mass = ''.join(map( lambda x : x.replace('_',''), result))
    allCards = [] 
    for dr in os.listdir(ls):
        if ls + '_' not in dr: continue
        if '.txt' not in dr: continue
        dat = open(ls + '/' + dr,'r')
        out = dat.read()
        dat.close()
        
        outdat = open('updated_cards/%s/%s'%(ls,dr),'w')
        outdat.write(out + '\n')
        outdat.write('lumiscale rateParam * * 1\n')
        outdat.write('nuisance edit freeze lumiscale\n')
        outdat.close()
        allCards.append( 'updated_cards/%s/%s'%(ls,dr) ) 
    # combine the cards 
    outCardName='updated_cards/%s/%s.txt'%(ls,ls)
    runIt('combineCards.py %s > %s'%(' '.join(allCards), outCardName))
    runIt('text2workspace.py -m {mass} {input} -o {output}'.format(mass=mass,
                                                                   input=outCardName, 
                                                                   output=outCardName.replace('.txt','.root')))
    runIt('combine -m {mass} -M AsymptoticLimits {output} --setParameters lumiscale=1 -t -1 --expectSignal=0'.format(mass=mass,
                                                                                        output=outCardName.replace('.txt','.root')))
    runIt('mv higgsCombineTest.AsymptoticLimits.mH{mass}.root cards2016/.'.format(mass=mass))
    runIt('combine -m {mass} -M AsymptoticLimits {output} --setParameters lumiscale=3.8 -t -1 --expectSignal=0'.format(mass=mass,
                                                                                                output=outCardName.replace('.txt','.root')))
    runIt('mv higgsCombineTest.AsymptoticLimits.mH{mass}.root cardsrun2/.'.format(mass=mass))
    runIt('combine -m {mass} -M AsymptoticLimits {output} --setParameters lumiscale=8.3 -t -1 --expectSignal=0'.format(mass=mass,
                                                                                                output=outCardName.replace('.txt','.root')))
    runIt('mv higgsCombineTest.AsymptoticLimits.mH{mass}.root cardsrun3/.'.format(mass=mass))


allDirectories = filter(lambda x : os.path.isdir(x), os.listdir('.'))
os.system('rm -r updated_cards')
os.mkdir('updated_cards')
pattern = '^[0-9]+_[0-9]+'
p = Pool(50)
p.map(makeTheThing, allDirectories)

    
