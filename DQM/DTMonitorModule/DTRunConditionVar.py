import FWCore.ParameterSet.Config as cms

def DTRunConditionVar(*args, **kwargs):
  mod = cms.EDProducer('DTRunConditionVar',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
