import FWCore.ParameterSet.Config as cms

def SiStripBadFiberDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripBadFiberDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
