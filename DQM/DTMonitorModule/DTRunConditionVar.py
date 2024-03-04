import FWCore.ParameterSet.Config as cms

def DTRunConditionVar(**kwargs):
  mod = cms.EDProducer('DTRunConditionVar',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
