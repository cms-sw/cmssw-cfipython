import FWCore.ParameterSet.Config as cms

def trgMatchedCandidateProducer(**kwargs):
  mod = cms.EDProducer('trgMatchedCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
