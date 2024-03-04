import FWCore.ParameterSet.Config as cms

def PATPackedCandidateProducer(**kwargs):
  mod = cms.EDProducer('PATPackedCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
