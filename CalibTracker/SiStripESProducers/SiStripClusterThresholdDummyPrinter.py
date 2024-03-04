import FWCore.ParameterSet.Config as cms

def SiStripClusterThresholdDummyPrinter(**kwargs):
  mod = cms.EDAnalyzer('SiStripClusterThresholdDummyPrinter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
