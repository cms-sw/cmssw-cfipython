import FWCore.ParameterSet.Config as cms

def trgMatchEcalCandidateProducer(**kwargs):
  mod = cms.EDProducer('trgMatchEcalCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
