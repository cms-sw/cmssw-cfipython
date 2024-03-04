import FWCore.ParameterSet.Config as cms

def DTLocalTriggerSynchTest(**kwargs):
  mod = cms.EDProducer('DTLocalTriggerSynchTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
