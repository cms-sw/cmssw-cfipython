import FWCore.ParameterSet.Config as cms

def ChargedRefCandidateProducer(**kwargs):
  mod = cms.EDProducer('ChargedRefCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
