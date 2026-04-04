import FWCore.ParameterSet.Config as cms

def ReadPixClusters(*args, **kwargs):
  mod = cms.EDAnalyzer('ReadPixClusters',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
