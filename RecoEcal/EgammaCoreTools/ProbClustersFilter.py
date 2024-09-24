import FWCore.ParameterSet.Config as cms

def ProbClustersFilter(*args, **kwargs):
  mod = cms.EDFilter('ProbClustersFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
