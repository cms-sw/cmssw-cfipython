import FWCore.ParameterSet.Config as cms

def DTLocalTriggerTask(*args, **kwargs):
  mod = cms.EDProducer('DTLocalTriggerTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
