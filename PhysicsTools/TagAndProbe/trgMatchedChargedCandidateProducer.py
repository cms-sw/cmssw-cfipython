import FWCore.ParameterSet.Config as cms

def trgMatchedChargedCandidateProducer(**kwargs):
  mod = cms.EDProducer('trgMatchedChargedCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
