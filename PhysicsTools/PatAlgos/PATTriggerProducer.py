import FWCore.ParameterSet.Config as cms

def PATTriggerProducer(**kwargs):
  mod = cms.EDProducer('PATTriggerProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
