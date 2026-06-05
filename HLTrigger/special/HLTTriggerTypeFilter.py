import FWCore.ParameterSet.Config as cms

def HLTTriggerTypeFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTTriggerTypeFilter',
    SelectedTriggerType = cms.int32(2),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
