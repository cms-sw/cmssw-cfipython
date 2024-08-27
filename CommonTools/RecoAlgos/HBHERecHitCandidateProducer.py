import FWCore.ParameterSet.Config as cms

def HBHERecHitCandidateProducer(**kwargs):
  mod = cms.EDProducer('HBHERecHitCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
