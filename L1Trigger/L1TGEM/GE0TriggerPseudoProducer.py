import FWCore.ParameterSet.Config as cms

def GE0TriggerPseudoProducer(**kwargs):
  mod = cms.EDProducer('GE0TriggerPseudoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
