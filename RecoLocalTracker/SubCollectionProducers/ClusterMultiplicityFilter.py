import FWCore.ParameterSet.Config as cms

def ClusterMultiplicityFilter(*args, **kwargs):
  mod = cms.EDFilter('ClusterMultiplicityFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
