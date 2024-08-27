import FWCore.ParameterSet.Config as cms

def SiStripGainDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripGainDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
