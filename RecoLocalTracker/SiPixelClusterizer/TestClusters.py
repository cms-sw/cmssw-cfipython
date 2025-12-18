import FWCore.ParameterSet.Config as cms

def TestClusters(*args, **kwargs):
  mod = cms.EDAnalyzer('TestClusters',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
