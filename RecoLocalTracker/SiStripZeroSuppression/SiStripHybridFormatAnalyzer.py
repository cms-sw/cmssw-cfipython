import FWCore.ParameterSet.Config as cms

def SiStripHybridFormatAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripHybridFormatAnalyzer',
    srcDigis = cms.InputTag('siStripZeroSuppression', 'VirginRaw'),
    srcAPVCM = cms.InputTag('siStripZeroSuppression', 'APVCMVirginRaw'),
    nModuletoDisplay = cms.uint32(10000),
    plotAPVCM = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
