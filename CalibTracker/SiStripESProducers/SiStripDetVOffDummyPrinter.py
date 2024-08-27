import FWCore.ParameterSet.Config as cms

def SiStripDetVOffDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripDetVOffDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
