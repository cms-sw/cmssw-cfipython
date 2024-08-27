import FWCore.ParameterSet.Config as cms

def DTRunConditionVarClient(**kwargs):
  mod = cms.EDProducer('DTRunConditionVarClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
