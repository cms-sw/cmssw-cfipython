import FWCore.ParameterSet.Config as cms

def RecAnalyzerHF(**kwargs):
  mod = cms.EDAnalyzer('RecAnalyzerHF',
    RunNZS = cms.bool(True),
    Noise = cms.bool(False),
    Ratio = cms.bool(False),
    ELowHF = cms.double(10),
    EHighHF = cms.double(150),
    TriggerBits = cms.untracked.vint32(),
    IgnoreL1 = cms.untracked.bool(False),
    FillHisto = cms.untracked.bool(False),
    HcalIeta = cms.untracked.vint32(),
    HcalIphi = cms.untracked.vint32(),
    HcalDepth = cms.untracked.vint32(),
    hfInput = cms.InputTag('hfprereco'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
