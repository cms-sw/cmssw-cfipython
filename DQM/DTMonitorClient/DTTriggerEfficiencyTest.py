import FWCore.ParameterSet.Config as cms

def DTTriggerEfficiencyTest(*args, **kwargs):
  mod = cms.EDProducer('DTTriggerEfficiencyTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
