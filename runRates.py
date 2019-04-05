import ROOT as r 


JetHT = [ 'HLT_AK8PFHT750_TrimMass50',
          'HLT_AK8PFHT800_TrimMass50',
          'HLT_AK8PFHT850_TrimMass50',
          'HLT_AK8PFHT900_TrimMass50',
          'HLT_AK8PFJet140',
          'HLT_AK8PFJet15',
          'HLT_AK8PFJet200',
          'HLT_AK8PFJet25',
          'HLT_AK8PFJet260',
          'HLT_AK8PFJet320',
          'HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p17',
          'HLT_AK8PFJet330_TrimMass30_PFAK8BTagDeepCSV_p1',
          'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np2',
          'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_np4',
          'HLT_AK8PFJet330_TrimMass30_PFAK8BoostedDoubleB_p02',
          'HLT_AK8PFJet360_TrimMass30',
          'HLT_AK8PFJet380_TrimMass30',
          'HLT_AK8PFJet400_TrimMass30',
          'HLT_AK8PFJet400',
          'HLT_AK8PFJet40',
          'HLT_AK8PFJet420_TrimMass30',
          'HLT_AK8PFJet450',
          'HLT_AK8PFJet500',
          'HLT_AK8PFJet550',
          'HLT_AK8PFJet60',
          'HLT_AK8PFJet80',
          'HLT_AK8PFJetFwd140',
          'HLT_AK8PFJetFwd15',
          'HLT_AK8PFJetFwd200',
          'HLT_AK8PFJetFwd25',
          'HLT_AK8PFJetFwd260',
          'HLT_AK8PFJetFwd320',
          'HLT_AK8PFJetFwd400',
          'HLT_AK8PFJetFwd40',
          'HLT_AK8PFJetFwd450',
          'HLT_AK8PFJetFwd500',
          'HLT_AK8PFJetFwd60',
          'HLT_AK8PFJetFwd80',
          'HLT_CaloJet500_NoJetID',
          'HLT_CaloJet550_NoJetID',
          'HLT_DiPFJetAve100_HFJEC',
          'HLT_DiPFJetAve140',
          'HLT_DiPFJetAve160_HFJEC',
          'HLT_DiPFJetAve200',
          'HLT_DiPFJetAve220_HFJEC',
          'HLT_DiPFJetAve260',
          'HLT_DiPFJetAve300_HFJEC',
          'HLT_DiPFJetAve320',
          'HLT_DiPFJetAve400',
          'HLT_DiPFJetAve40',
          'HLT_DiPFJetAve500',
          'HLT_DiPFJetAve60_HFJEC',
          'HLT_DiPFJetAve60',
          'HLT_DiPFJetAve80_HFJEC',
          'HLT_DiPFJetAve80',
          'HLT_DoublePFJets100_CaloBTagDeepCSV_p71',
          'HLT_DoublePFJets116MaxDeta1p6_DoubleCaloBTagDeepCSV_p71',
          'HLT_DoublePFJets128MaxDeta1p6_DoubleCaloBTagDeepCSV_p71',
          'HLT_DoublePFJets200_CaloBTagDeepCSV_p71',
          'HLT_DoublePFJets350_CaloBTagDeepCSV_p71',
          'HLT_DoublePFJets40_CaloBTagDeepCSV_p71',
          'HLT_Mu12_DoublePFJets100_CaloBTagDeepCSV_p71',
          'HLT_Mu12_DoublePFJets200_CaloBTagDeepCSV_p71',
          'HLT_Mu12_DoublePFJets350_CaloBTagDeepCSV_p71',
          'HLT_Mu12_DoublePFJets40MaxDeta1p6_DoubleCaloBTagDeepCSV_p71',
          'HLT_Mu12_DoublePFJets40_CaloBTagDeepCSV_p71',
          'HLT_Mu12_DoublePFJets54MaxDeta1p6_DoubleCaloBTagDeepCSV_p71',
          'HLT_Mu12_DoublePFJets62MaxDeta1p6_DoubleCaloBTagDeepCSV_p71',
          'HLT_PFHT1050',
          'HLT_PFHT180',
          'HLT_PFHT250',
          'HLT_PFHT330PT30_QuadPFJet_75_60_45_40_TriplePFBTagDeepCSV_4p5',
          'HLT_PFHT330PT30_QuadPFJet_75_60_45_40',
          'HLT_PFHT350MinPFJet15',
          'HLT_PFHT350',
          'HLT_PFHT370',
          'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94',
          'HLT_PFHT400_SixPFJet32',
          'HLT_PFHT430',
          'HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59',
          'HLT_PFHT450_SixPFJet36',
          'HLT_PFHT500_PFMET100_PFMHT100_IDTight',
          'HLT_PFHT500_PFMET110_PFMHT110_IDTight',
          'HLT_PFHT510',
          'HLT_PFHT590',
          'HLT_PFHT680',
          'HLT_PFHT700_PFMET85_PFMHT85_IDTight',
          'HLT_PFHT700_PFMET95_PFMHT95_IDTight',
          'HLT_PFHT780',
          'HLT_PFHT800_PFMET75_PFMHT75_IDTight',
          'HLT_PFHT800_PFMET85_PFMHT85_IDTight',
          'HLT_PFHT890',
          'HLT_PFJet140',
          'HLT_PFJet15',
          'HLT_PFJet200',
          'HLT_PFJet25',
          'HLT_PFJet260',
          'HLT_PFJet320',
          'HLT_PFJet400',
          'HLT_PFJet40',
          'HLT_PFJet450',
          'HLT_PFJet500',
          'HLT_PFJet550',
          'HLT_PFJet60',
          'HLT_PFJet80',
          'HLT_PFJetFwd140',
          'HLT_PFJetFwd15',
          'HLT_PFJetFwd200',
          'HLT_PFJetFwd25',
          'HLT_PFJetFwd260',
          'HLT_PFJetFwd320',
          'HLT_PFJetFwd400',
          'HLT_PFJetFwd40',
          'HLT_PFJetFwd450',
          'HLT_PFJetFwd500',
          'HLT_PFJetFwd60',
          'HLT_PFJetFwd80',
          'HLT_QuadPFJet103_88_75_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1',
          'HLT_QuadPFJet103_88_75_15_PFBTagDeepCSV_1p3_VBF2',
          'HLT_QuadPFJet103_88_75_15',
          'HLT_QuadPFJet105_88_76_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1',
          'HLT_QuadPFJet105_88_76_15_PFBTagDeepCSV_1p3_VBF2',
          'HLT_QuadPFJet105_88_76_15',
          'HLT_QuadPFJet111_90_80_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1',
          'HLT_QuadPFJet111_90_80_15_PFBTagDeepCSV_1p3_VBF2',
          'HLT_QuadPFJet111_90_80_15',
          'HLT_QuadPFJet98_83_71_15_DoublePFBTagDeepCSV_1p3_7p7_VBF1',
          'HLT_QuadPFJet98_83_71_15_PFBTagDeepCSV_1p3_VBF2',
          'HLT_QuadPFJet98_83_71_15',
          'HLT_Rsq0p35',
          'HLT_Rsq0p40',
          'HLT_RsqMR300_Rsq0p09_MR200_4jet',
          'HLT_RsqMR300_Rsq0p09_MR200',
          'HLT_RsqMR320_Rsq0p09_MR200_4jet',
          'HLT_RsqMR320_Rsq0p09_MR200',
          'HLT_SingleJet30_Mu12_SinglePFJet40' ]

import os 
Events = r.TChain("Events")
for i in os.listdir('.'):
    if '.root' not in i: continue
    Events.Add(i)
lumis = []
print 'About to process', Events.GetEntries()

counts = {}

paths = [
    'HLT_PFHT400_SixPFJet32_DoublePFBTagDeepCSV_2p94',
    'HLT_PFHT450_SixPFJet36_PFBTagDeepCSV_1p59',
    'HLT_PFHT450_SixPFJet36',
    'HLT_PFHT400_SixPFJet32',
    'HLT_PFHT430',
    ]

control = [
    'HLT_PFHT450_SixPFJet36',
    'HLT_PFHT400_SixPFJet32',
    'HLT_PFHT430',
]

for path in paths: 
    counts[path]=0
    counts[path+'_pure']=0

counts['TOP']=0
counts['TOP_pure']=0
counts['TOP_control']=0
counts['TOP_control_pure']=0


nevs = 0 

# tfile = r.TFile.Open('skimmed.root','recreate')
# Event_copy = Events.CopyTree("run == 319639")
# Event_copy.AutoSave()
# tfile.Close()
# print Event_copy.GetEntries(), 'events after skimming' 

#print kk 
tfile = r.TFile.Open('skimmed.root')
Event_copy = tfile.Events


def countSet(paths, dataset):
    passed, isPure = False , False 
    for path in paths:
        if getattr(ev,path): 
            passed=True
            break
    if not passed: return False, False 
    passed, isPure = True, True
    for path2 in dataset:
        if path2 in paths: continue
        if getattr(ev,path2): 
            isPure=False
            break 
    return passed, isPure

for ev in Event_copy:
    nevs+=1
    #if ev.run != 319639: continue 
    if nevs%100000==0: 
        print 'processed', nevs
        print counts, len(lumis)
        break
    if ev.luminosityBlock not in lumis: lumis.append(ev.luminosityBlock)
    
    for path in paths:
        passed, isPure = countSet([path], JetHT)
        counts[path] += passed
        counts[path+'_pure'] += isPure
    passed, isPure = countSet(paths, JetHT); counts['TOP'] += passed; counts['TOP_pure'] += isPure
    passed, isPure = countSet(control, JetHT); counts['TOP_control'] += passed; counts['TOP_control_pure'] += isPure

print counts, len(lumis)

for k, count in counts.iteritems():
    print k, count, count/(len(lumis)*23.31)
