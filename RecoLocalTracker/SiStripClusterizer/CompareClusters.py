import FWCore.ParameterSet.Config as cms

def CompareClusters(*args, **kwargs):
  mod = cms.EDAnalyzer('CompareClusters',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
