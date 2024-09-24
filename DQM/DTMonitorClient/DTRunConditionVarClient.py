import FWCore.ParameterSet.Config as cms

def DTRunConditionVarClient(*args, **kwargs):
  mod = cms.EDProducer('DTRunConditionVarClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
