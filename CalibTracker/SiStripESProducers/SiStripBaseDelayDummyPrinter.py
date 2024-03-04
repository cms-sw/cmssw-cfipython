import FWCore.ParameterSet.Config as cms

def SiStripBaseDelayDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripBaseDelayDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
