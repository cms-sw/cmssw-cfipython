import FWCore.ParameterSet.Config as cms

def PATTriggerProducer(*args, **kwargs):
  mod = cms.EDProducer('PATTriggerProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
