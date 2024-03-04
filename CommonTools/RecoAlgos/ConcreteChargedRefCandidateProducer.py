import FWCore.ParameterSet.Config as cms

def ConcreteChargedRefCandidateProducer(**kwargs):
  mod = cms.EDProducer('ConcreteChargedRefCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
