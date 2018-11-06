import ROOT as r 
import os
import copy

r.gROOT.SetBatch(True)
r.gStyle.SetPaintTextFormat('4.1f')
class binning:
    def __init__(self, mi, ma, w):
        self._min = mi
        self._max = ma
        self.w  = w 
        self.n  = abs(ma-mi)/w

class Scan:
    def __init__(self,name):
        if name == 'CharNeu_Moriond2017':
            self.xbins = binning(100,700,25)
            self.ybins = binning(0,300,1)
        else: raise RuntimeError('wrong scan name')

scan = Scan('CharNeu_Moriond2017')

for reference in 'cards2016,cardsrun2,cardsrun3'.split(','):
    os.system('hadd {ref}/allLimits.root {ref}/*.root'.format(ref=reference))
    fil = r.TFile('{ref}/allLimits.root'.format(ref=reference))
    limit = fil.Get('limit')
    
    ex_obs = r.TH2F('ex_obs', '', 
                    scan.xbins.n+1, scan.xbins._min-scan.xbins.w/2.,
                    scan.xbins._max+scan.xbins.w/2., scan.ybins.n+1,
                    scan.ybins._min-scan.ybins.w/2., 
                    scan.ybins._max+scan.ybins.w/2.)
                               
    for point in limit:
        limit     = point.limit
        mass      = str(int(point.mh))
        if len(mass) > 6:
            massx     = int(mass[:4]); massy = int(mass[4:])
        else:
            massx     = int(mass[:3]); massy = int(mass[3:])

        if 0.49 < point.quantileExpected < 0.51:
            ex_obs    .Fill(massx, massy, limit)

    c = r.TCanvas()
    ex_obs.Draw('colz text')
    c.SaveAs('text_%s.pdf'%reference)
    c.SaveAs('text_%s.png'%reference)
        

    ex_obs.GetZaxis().SetRangeUser(0,10)
    gr2d = r.TGraph2D(ex_obs)


    xbinsize = 12.5; ybinsize = 12.5
    gr2d.SetNpx( int((gr2d.GetXmax() - gr2d.GetXmin())/xbinsize) )
    gr2d.SetNpy( int((gr2d.GetYmax() - gr2d.GetYmin())/ybinsize) )
    tmp_2d_histo = gr2d.GetHistogram()
    tmp_graph_list = gr2d.GetContourList(1.0)
    # print ex_obs.GetMaximum(), ex_obs.GetMinimum()
    # for i in range(ex_obs.GetXaxis().GetNbins()):
    #     for j  in range(ex_obs.GetXaxis().GetNbins()):
    #         if ex_obs.GetBinContent( ex_obs.GetBin(i,j)): print ex_obs.GetBinContent( ex_obs.GetBin(i,j))

    tmp_graph = tmp_graph_list[max( (i.GetN(),j) for j,i in enumerate( tmp_graph_list )  )[1]]
    h_smoothed = tmp_2d_histo.Clone('smoothedGraph')
    smoothedbins = []
    for i in range(h_smoothed.GetNbinsX()+1):
        for j in range(h_smoothed.GetNbinsY()+1):
            if j > 0 and not h_smoothed.GetBinContent(i,j):
                h_smoothed.SetBinContent(i,j,h_smoothed.GetBinContent(i-1,j))
                smoothedbins.append((i,j))
                break
    h_smoothed.Smooth(1, 'k3a')
    for i,j in smoothedbins:
        h_smoothed.SetBinContent(i,j,0.)


    smcopy = copy.deepcopy(h_smoothed)
    smoothed_2dg = r.TGraph2D(smcopy)
    xbinsize = 5.; ybinsize = 5.
    smoothed_2dg.SetNpx( int((smoothed_2dg.GetXmax() - smoothed_2dg.GetXmin())/xbinsize) )
    smoothed_2dg.SetNpy( int((smoothed_2dg.GetYmax() - smoothed_2dg.GetYmin())/ybinsize) )
    brunosucksballs = smoothed_2dg.GetHistogram() ## have to call this, otherwise root will freak out
    c = smoothed_2dg.GetContourList(1.0)
    smoothed_g   = c[max( (i.GetN(),j) for j,i in enumerate( c )  )[1]]
    smoothed_2dg.GetZaxis().SetRangeUser(0,10)
    c = r.TCanvas()
    smoothed_2dg.Draw('colz')
    c.SaveAs('%s.pdf'%reference)
    c.SaveAs('%s.png'%reference)

    
    outfile = r.TFile.Open('%s.root'%reference,'recreate') 
    smoothed_g.Write()
    outfile.Close()



