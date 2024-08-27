import FWCore.ParameterSet.Config as cms

def DTTriggerEfficiencyTest(**kwargs):
  mod = cms.EDProducer('DTTriggerEfficiencyTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
