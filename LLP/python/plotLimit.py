import os
import sys
import numpy
import math
import ROOT

# ROOT.gStyle.SetHistFillStyle(0)
# ROOT.gStyle.SetLegoInnerR(Float_t rad = 0.5)
# ROOT.gStyle.SetNumberContours(Int_t number = 20)
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetEndErrorSize(2)
#ROOT.gStyle.SetErrorMarker(20)
ROOT.gStyle.SetErrorX(0.)

ROOT.gStyle.SetMarkerStyle(20)
#ROOT.gStyle.SetMarkerStyle(20)

#For the fit/function:
ROOT.gStyle.SetOptFit(1)
ROOT.gStyle.SetFitFormat("5.4g")
ROOT.gStyle.SetFuncColor(2)
ROOT.gStyle.SetFuncStyle(1)
ROOT.gStyle.SetFuncWidth(1)

#For the date:
ROOT.gStyle.SetOptDate(0)
# ROOT.gStyle.SetDateX(Float_t x = 0.01)
# ROOT.gStyle.SetDateY(Float_t y = 0.01)

# For the statistics box:
ROOT.gStyle.SetOptFile(0)
ROOT.gStyle.SetOptStat(0) # To display the mean and RMS:   SetOptStat("mr")
ROOT.gStyle.SetStatColor(ROOT.kWhite)
ROOT.gStyle.SetStatFont(42)
ROOT.gStyle.SetStatFontSize(0.025)
ROOT.gStyle.SetStatTextColor(1)
ROOT.gStyle.SetStatFormat("6.4g")
ROOT.gStyle.SetStatBorderSize(1)
ROOT.gStyle.SetStatH(0.1)
ROOT.gStyle.SetStatW(0.15)

ROOT.gStyle.SetHatchesSpacing(1)
ROOT.gStyle.SetHatchesLineWidth(2)

# ROOT.gStyle.SetStaROOT.TStyle(Style_t style = 1001)
# ROOT.gStyle.SetStatX(Float_t x = 0)
# ROOT.gStyle.SetStatY(Float_t y = 0)


#ROOT.gROOT.ForceStyle(True)
#end modified

# For the Global title:

ROOT.gStyle.SetOptTitle(0)



# ROOT.gStyle.SetTitleH(0) # Set the height of the title box
# ROOT.gStyle.SetTitleW(0) # Set the width of the title box
#ROOT.gStyle.SetTitleX(0.35) # Set the position of the title box
#ROOT.gStyle.SetTitleY(0.986) # Set the position of the title box
# ROOT.gStyle.SetTitleStyle(Style_t style = 1001)
#ROOT.gStyle.SetTitleBorderSize(0)

# For the axis titles:
ROOT.gStyle.SetTitleColor(1, "XYZ")
ROOT.gStyle.SetTitleFont(43, "XYZ")
ROOT.gStyle.SetTitleSize(35, "XYZ")
# ROOT.gStyle.SetTitleXSize(Float_t size = 0.02) # Another way to set the size?
# ROOT.gStyle.SetTitleYSize(Float_t size = 0.02)
ROOT.gStyle.SetTitleXOffset(1.2)
#ROOT.gStyle.SetTitleYOffset(1.2)
ROOT.gStyle.SetTitleOffset(1.45, "YZ") # Another way to set the Offset

# For the axis labels:

ROOT.gStyle.SetLabelColor(1, "XYZ")
ROOT.gStyle.SetLabelFont(43, "XYZ")
ROOT.gStyle.SetLabelOffset(0.0077, "XYZ")
ROOT.gStyle.SetLabelSize(29, "XYZ")
#ROOT.gStyle.SetLabelSize(0.04, "XYZ")

# For the axis:

ROOT.gStyle.SetAxisColor(1, "XYZ")
ROOT.gStyle.SetAxisColor(1, "XYZ")
ROOT.gStyle.SetStripDecimals(True)
ROOT.gStyle.SetTickLength(0.025, "Y")
ROOT.gStyle.SetTickLength(0.025, "X")


ROOT.gStyle.SetPadTickX(1)  # To get tick marks on the opposite side of the frame
ROOT.gStyle.SetPadTickY(1)

# Change for log plots:
ROOT.gStyle.SetOptLogx(0)
ROOT.gStyle.SetOptLogy(0)
ROOT.gStyle.SetOptLogz(0)

#ROOT.gStyle.SetPalette(1) #(1,0)

# another top group addition

# Postscript options:
#ROOT.gStyle.SetPaperSize(20., 20.)
#ROOT.gStyle.SetPaperSize(ROOT.TStyle.kA4)
#ROOT.gStyle.SetPaperSize(27., 29.7)
#ROOT.gStyle.SetPaperSize(27., 29.7)
ROOT.gStyle.SetPaperSize(8.5*1.4,7.0*1.4)
ROOT.TGaxis.SetMaxDigits(3)
ROOT.gStyle.SetLineScalePS(2)

# ROOT.gStyle.SetLineStyleString(Int_t i, const char* text)
# ROOT.gStyle.SetHeaderPS(const char* header)
# ROOT.gStyle.SetTitlePS(const char* pstitle)
#ROOT.gStyle.SetColorModelPS(1)

# ROOT.gStyle.SetBarOffset(Float_t baroff = 0.5)
# ROOT.gStyle.SetBarWidth(Float_t barwidth = 0.5)
# ROOT.gStyle.SetPaintTextFormat(const char* format = "g")
# ROOT.gStyle.SetPalette(Int_t ncolors = 0, Int_t* colors = 0)
# ROOT.gStyle.SetTimeOffset(Double_t toffset)
# ROOT.gStyle.SetHistMinimumZero(kTRUE)

ROOT.gStyle.SetPaintTextFormat("3.0f")

NRGBs = 5;
NCont = 255;

stops = numpy.array( [0.00, 0.34, 0.61, 0.84, 1.00] )
red  = numpy.array( [0.00, 0.00, 0.87, 1.00, 0.51] )
green = numpy.array( [0.00, 0.81, 1.00, 0.20, 0.00] )
blue = numpy.array( [0.51, 1.00, 0.12, 0.00, 0.00] )

colWheelDark = ROOT.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)

for i in range(NRGBs):
    red[i]=min(1,red[i]*1.1+0.25)
    green[i]=min(1,green[i]*1.1+0.25)
    blue[i]=min(1,blue[i]*1.1+0.25)

colWheel = ROOT.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)
ROOT.gStyle.SetNumberContours(NCont)
ROOT.gRandom.SetSeed(123)

colors=[]
def hex2rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16)/255.0 for i in range(0, lv, lv // 3))

def newColor(red,green,blue):
    newColor.colorindex+=1
    color=ROOT.TColor(newColor.colorindex,red,green,blue)
    colors.append(color)
    return color
    
newColor.colorindex=301

def getDarkerColor(color):
    darkerColor=newColor(color.GetRed()*0.6,color.GetGreen()*0.6,color.GetBlue()*0.6)
    return darkerColor

massesDict = {
    600:[0,200,400,500],
    800:[0,200,400,600,700],
    1000:[0,200,400,600,800,900],
    1200:[0,200,400,600,800,900,1000,1100],
    1400:[0,200,400,600,800,900,1000,1200,1300],
    1600:[0,200,400,600,800,900,1000,1200,1400],
    1800:[0,200,400,600,800,1000,1200,1400],
    2000:[0,200,400,600,800,1000,1200,1400],
    2200:[0,200,400,600,800,1000,1200,1400],
    2400:[0,200,400,600,800,1000,1200,1400]
}

def parseCombineResult(filePath):
    rootFile = ROOT.TFile(filePath)
    limitTree = rootFile.Get("limit")
    result = {}
    #note: combine seems to be not very precise here
    mapping = {
        "median": 0.5, 
        "+1":0.840, 
        "-1":0.160,
        "+2":0.975,
        "-2":0.025
    }
    for entry in range(limitTree.GetEntries()):
        limitTree.GetEntry(entry)
        found = False
        for k,v in mapping.iteritems():
            if math.fabs(limitTree.quantileExpected-v)<0.0001:
                result[k] = limitTree.limit
                found = True
                break
        if not found and limitTree.quantileExpected>0:
            print "unknown quantile: ",limitTree.quantileExpected

    return result

basePath = "cards"

results = {}

for ctau in [1]:
    results[ctau] = {}
    for llpMass in sorted(massesDict.keys()):
        results[ctau][llpMass] = {}
        for lspMass in massesDict[llpMass]:
            signalProcess = "ctau%i_llp%i_lsp%i"%(ctau,llpMass,lspMass)
            combineOutputFile = os.path.join(basePath,signalProcess,"higgsCombineTest.AsymptoticLimits.mH120.root")
            result = parseCombineResult(combineOutputFile)
            if len(result.keys())!=5:
                print "WARNING: Not all quantiles found in file ",combineOutputFile
            if not result.has_key("median"):
                print "ERROR: Median found in file ",combineOutputFile," -> skip"
            else:
                results[ctau][llpMass][lspMass] = result
                
   
for ctau in results.keys():
    cv = ROOT.TCanvas("cv","",850,700)
    cv.SetLeftMargin(0.145)
    cv.SetRightMargin(0.195)
    cv.SetBottomMargin(0.14)
    cv.SetTopMargin(0.08)
    xmin = 600
    ymin = 0
    xmax = 2400
    ymax = 1600
    print numpy.linspace(xmin-25,xmax+25,(xmax-xmin)/50+2)
    axis = ROOT.TH2F("axis",";m#lower[0.2]{#scale[0.8]{#tilde{g}}} (GeV); m#lower[0.2]{#scale[0.8]{#tilde{#chi}#lower[-0.5]{#scale[0.65]{0}}#kern[-1.2]{#lower[0.6]{#scale[0.65]{1}}}}} (GeV)",
        (xmax-xmin)/50+1,numpy.linspace(xmin-25,xmax+25,(xmax-xmin)/50+2),
        (ymax-ymin)/50+1,numpy.linspace(ymin-25,ymax+25,(ymax-ymin)/50+2)
    )
    for xbin in range(axis.GetNbinsX()):
        value = xmin+xbin*(xmax-xmin)/50
        if xbin%4==0:
            axis.GetXaxis().SetBinLabel(xbin+1,"%.0f"%axis.GetXaxis().GetBinCenter(xbin+1))
    for llpMass in sorted(results[ctau].keys()):
        for lspMass in sorted(results[ctau][llpMass].keys()):
            axis.Fill(llpMass,lspMass,results[ctau][llpMass][lspMass]["median"])
    
    axis.Draw("colz")
    axis.GetZaxis().SetTitle("95% CL upper limit on #sigma (pb)")
    axis.GetZaxis().Set(50,0.0005,0.5)
    axis.GetZaxis().SetRangeUser(0.0005,0.5)
    cv.SetLogz(1)
    axis.GetXaxis().SetNoExponent(True)
    #axis.GetXaxis().LabelsOption("v")
    axis.GetYaxis().SetNoExponent(True)
    axis.GetXaxis().SetNdivisions(510)
    axis.GetYaxis().SetNdivisions(510)
    
    poly = ROOT.TPolyLine(3,
        numpy.array([600-25,1600+25,600-25],dtype=numpy.float32), 
        numpy.array([600-25,1600+25,1600+25],dtype=numpy.float32),
    )
    poly.SetFillColor(ROOT.kGray)
    poly.SetFillStyle(3445)
    poly.Draw("F")
    
    ROOT.gPad.RedrawAxis()
    
    cv.Print("limits_ctau%i.pdf"%ctau)
    cv.Print("limits_ctau%i.png"%ctau)
    
    

