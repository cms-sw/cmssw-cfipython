import FWCore.ParameterSet.Config as cms

def DTLocalTriggerTest(*args, **kwargs):
  mod = cms.EDProducer('DTLocalTriggerTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod