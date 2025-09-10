import FWCore.ParameterSet.Config as cms

def PATTriggerEventProducer(*args, **kwargs):
  mod = cms.EDProducer('PATTriggerEventProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
