import FWCore.ParameterSet.Config as cms

def SiStripDetCablingDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripDetCablingDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
