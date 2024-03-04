import FWCore.ParameterSet.Config as cms

def ClusterMTCCFilter(**kwargs):
  mod = cms.EDFilter('ClusterMTCCFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
