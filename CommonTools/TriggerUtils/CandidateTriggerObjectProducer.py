import FWCore.ParameterSet.Config as cms

def CandidateTriggerObjectProducer(**kwargs):
  mod = cms.EDProducer('CandidateTriggerObjectProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
