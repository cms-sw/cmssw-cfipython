import FWCore.ParameterSet.Config as cms

def trgMatchChargedCandidateProducer(**kwargs):
  mod = cms.EDProducer('trgMatchChargedCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
