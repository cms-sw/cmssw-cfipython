import FWCore.ParameterSet.Config as cms

def ME0TriggerProducer(**kwargs):
  mod = cms.EDProducer('ME0TriggerProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
