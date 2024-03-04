import FWCore.ParameterSet.Config as cms

def ReadPixClusters(**kwargs):
  mod = cms.EDAnalyzer('ReadPixClusters',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
