import FWCore.ParameterSet.Config as cms

def ClusterMTCCFilter(*args, **kwargs):
  mod = cms.EDFilter('ClusterMTCCFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
