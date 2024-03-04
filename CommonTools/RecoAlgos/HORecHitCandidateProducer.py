import FWCore.ParameterSet.Config as cms

def HORecHitCandidateProducer(**kwargs):
  mod = cms.EDProducer('HORecHitCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
