import FWCore.ParameterSet.Config as cms

def L1GtTriggerMenuLiteProducer(*args, **kwargs):
  mod = cms.EDProducer('L1GtTriggerMenuLiteProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
