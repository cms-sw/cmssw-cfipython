import FWCore.ParameterSet.Config as cms

def ChargedCandidateProducer(**kwargs):
  mod = cms.EDProducer('ChargedCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
