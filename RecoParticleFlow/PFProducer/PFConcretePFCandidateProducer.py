import FWCore.ParameterSet.Config as cms

def PFConcretePFCandidateProducer(**kwargs):
  mod = cms.EDProducer('PFConcretePFCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
