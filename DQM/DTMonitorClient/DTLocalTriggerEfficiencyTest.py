import FWCore.ParameterSet.Config as cms

def DTLocalTriggerEfficiencyTest(*args, **kwargs):
  mod = cms.EDProducer('DTLocalTriggerEfficiencyTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
