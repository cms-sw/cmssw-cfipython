import FWCore.ParameterSet.Config as cms

def DTLocalTriggerTask(**kwargs):
  mod = cms.EDProducer('DTLocalTriggerTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
