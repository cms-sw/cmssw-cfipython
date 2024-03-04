import FWCore.ParameterSet.Config as cms

def SiStripDelayDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripDelayDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
