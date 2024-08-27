import FWCore.ParameterSet.Config as cms

def SiStripThresholdDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripThresholdDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
