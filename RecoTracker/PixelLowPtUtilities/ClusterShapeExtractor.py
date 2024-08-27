import FWCore.ParameterSet.Config as cms

def ClusterShapeExtractor(**kwargs):
  mod = cms.EDAnalyzer('ClusterShapeExtractor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
