import FWCore.ParameterSet.Config as cms

def TECClusterFilter(*args, **kwargs):
  mod = cms.EDFilter('TECClusterFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
