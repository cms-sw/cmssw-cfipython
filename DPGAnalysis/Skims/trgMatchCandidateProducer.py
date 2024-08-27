import FWCore.ParameterSet.Config as cms

def trgMatchCandidateProducer(**kwargs):
  mod = cms.EDProducer('trgMatchCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
