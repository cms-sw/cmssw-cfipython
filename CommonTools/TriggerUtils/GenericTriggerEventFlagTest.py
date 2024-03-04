import FWCore.ParameterSet.Config as cms

def GenericTriggerEventFlagTest(**kwargs):
  mod = cms.EDFilter('GenericTriggerEventFlagTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
