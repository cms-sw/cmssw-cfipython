import FWCore.ParameterSet.Config as cms

def DTTriggerEfficiencyTask(**kwargs):
  mod = cms.EDProducer('DTTriggerEfficiencyTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
