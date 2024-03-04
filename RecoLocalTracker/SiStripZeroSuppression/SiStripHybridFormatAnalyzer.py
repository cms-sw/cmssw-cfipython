import FWCore.ParameterSet.Config as cms

def SiStripHybridFormatAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SiStripHybridFormatAnalyzer',
    srcDigis = cms.InputTag('siStripZeroSuppression', 'VirginRaw'),
    srcAPVCM = cms.InputTag('siStripZeroSuppression', 'APVCMVirginRaw'),
    nModuletoDisplay = cms.uint32(10000),
    plotAPVCM = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
