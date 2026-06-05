import FWCore.ParameterSet.Config as cms

def DTTriggerEfficiencyTask(*args, **kwargs):
  mod = cms.EDProducer('DTTriggerEfficiencyTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
