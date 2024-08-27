import FWCore.ParameterSet.Config as cms

def TECClusterFilter(**kwargs):
  mod = cms.EDFilter('TECClusterFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
