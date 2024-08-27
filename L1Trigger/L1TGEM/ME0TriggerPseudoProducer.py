import FWCore.ParameterSet.Config as cms

def ME0TriggerPseudoProducer(**kwargs):
  mod = cms.EDProducer('ME0TriggerPseudoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
