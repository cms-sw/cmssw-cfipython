import FWCore.ParameterSet.Config as cms

def CompareClusters(**kwargs):
  mod = cms.EDAnalyzer('CompareClusters',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
