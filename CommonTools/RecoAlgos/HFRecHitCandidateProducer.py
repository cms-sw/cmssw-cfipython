import FWCore.ParameterSet.Config as cms

def HFRecHitCandidateProducer(**kwargs):
  mod = cms.EDProducer('HFRecHitCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
