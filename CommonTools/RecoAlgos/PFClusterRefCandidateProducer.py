import FWCore.ParameterSet.Config as cms

def PFClusterRefCandidateProducer(**kwargs):
  mod = cms.EDProducer('PFClusterRefCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
