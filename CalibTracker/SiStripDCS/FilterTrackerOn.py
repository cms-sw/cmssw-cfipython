import FWCore.ParameterSet.Config as cms

def FilterTrackerOn(*args, **kwargs):
  mod = cms.EDFilter('FilterTrackerOn',
    MinModulesWithHVoff = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
