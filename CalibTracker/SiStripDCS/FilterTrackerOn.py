import FWCore.ParameterSet.Config as cms

def FilterTrackerOn(**kwargs):
  mod = cms.EDFilter('FilterTrackerOn',
    MinModulesWithHVoff = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
