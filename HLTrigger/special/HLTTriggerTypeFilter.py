import FWCore.ParameterSet.Config as cms

def HLTTriggerTypeFilter(**kwargs):
  mod = cms.EDFilter('HLTTriggerTypeFilter',
    SelectedTriggerType = cms.int32(2),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
